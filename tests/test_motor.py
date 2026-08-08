import unittest

from motor_triagem import Motor, Resultado, Sessao
from motor_triagem.__main__ import executar_cenario

BASE_SAUDAVEL = {
    "cirurgia_eletiva": True,
    "sca_recente": False, "ic_descompensada": False,
    "arritmia_grave": False, "valvopatia_grave_sintomatica": False,
    "hist_doenca_coronariana": False, "hist_avc_ait": False,
    "insuficiencia_cardiaca_historia": False, "fe_reduzida": "nao",
    "marcapasso": False, "dialise": "nao", "doenca_renal_cronica": False,
    "diabetes": "nao", "hipertensao": "nao", "dpoc": False,
    "doenca_pulmonar_leve": False, "hepatite_ativa": False,
    "alcool": "ausente_minimo", "tabagismo_atual": False, "imc": 24,
    "gestacao": "nao_se_aplica", "limitacao_funcional_substantiva": False,
    "outra_doenca": "nenhuma", "mets_4": "sim",
}


class TestMotor(unittest.TestCase):
    def setUp(self):
        self.motor = Motor()

    def executa(self, **respostas):
        return executar_cenario(self.motor, respostas)

    # ---------------- Caminhos de saída precoce ----------------
    def test_menor_de_idade_fora_de_escopo(self):
        res = self.executa(idade=15)
        self.assertEqual(res.saida, "fora_de_escopo")

    def test_cirurgia_nao_eletiva_fora_de_escopo(self):
        res = self.executa(idade=40, cirurgia_eletiva=False)
        self.assertEqual(res.saida, "fora_de_escopo")

    def test_instabilidade_suspende(self):
        res = self.executa(idade=58, cirurgia_eletiva=True, sca_recente=False, ic_descompensada=True)
        self.assertEqual(res.saida, "suspender_indicacao")
        self.assertEqual(res.sinalizadores[0]["id"], "instabilidade_cardiaca")
        self.assertEqual(res.trajeto[-1], "N1")

    def test_asa_iv_evento_recente_suspende(self):
        respostas = dict(BASE_SAUDAVEL, idade=60, procedimento="colecistectomia",
                         hist_doenca_coronariana=True, evento_timing="menos_3_meses")
        res = self.executa(**respostas)
        self.assertEqual(res.saida, "suspender_indicacao")
        self.assertEqual(res.asa, "IV")
        self.assertEqual(res.sinalizadores[0]["id"], "asa_iv_provisorio")

    # ---------------- Gate liberado ----------------
    def test_jovem_saudavel_liberado_sem_exames(self):
        res = self.executa(idade=34, procedimento="catarata", **BASE_SAUDAVEL)
        self.assertEqual(res.saida, "plano")
        self.assertEqual(res.asa, "I")
        self.assertEqual(res.porte, "baixo")
        self.assertNotIn("N6", res.trajeto)
        self.assertIn("N11", res.trajeto)
        # Nenhum exame de rotina obrigatório
        recomendados = [e for e, i in res.exames.items() if i["recomendacao"] == "sim"]
        self.assertEqual(recomendados, [])

    def test_liberado_com_capacidade_ruim_sinaliza_prehab(self):
        respostas = dict(BASE_SAUDAVEL, mets_4="nao")
        res = self.executa(idade=40, procedimento="hernia inguinal", **respostas)
        self.assertEqual(res.saida, "plano")
        ids = [s["id"] for s in res.sinalizadores]
        self.assertIn("pre_habilitacao", ids)

    # ---------------- Braço de risco ----------------
    def test_idoso_de_risco_porte_alto(self):
        respostas = dict(
            BASE_SAUDAVEL, idade=72,
            procedimento="aneurisma de aorta abdominal",
            hist_doenca_coronariana=True, evento_timing="3_meses_ou_mais",
            diabetes="mal_controlado", diabetes_insulina=True,
            hipertensao="mal_controlada", tabagismo_atual=True,
            frail_score=2, mets_4="nao",
            ecg_12m=False, anticoagulante=False,
            sopro_com_sintoma=False, sinais_ic=False, hba1c_3m=False,
        )
        res = self.executa(idade=72, **{k: v for k, v in respostas.items() if k != "idade"})
        self.assertEqual(res.saida, "plano")
        self.assertEqual(res.asa, "III")
        self.assertEqual(res.porte, "alto")
        # Pacote ESC de entrada
        self.assertEqual(res.exames["ecg_repouso"]["recomendacao"], "sim")
        self.assertEqual(res.exames["nt_probnp_bnp"]["recomendacao"], "sim")
        self.assertEqual(res.exames["hs_ctn_basal"]["recomendacao"], "sim")
        # NICE: porte alto → hemograma para todos; renal sim para ASA III
        self.assertEqual(res.exames["hemograma_completo"]["recomendacao"], "sim")
        self.assertEqual(res.exames["funcao_renal_creatinina_eletrolitos"]["recomendacao"], "sim")
        # HbA1c sem resultado recente → sim
        self.assertEqual(res.exames["hba1c"]["recomendacao"], "sim")
        # RCRI: porte alto + coronariopatia + insulina = 3 → risco alto
        self.assertEqual(res.rcri["escore"], 3)
        self.assertEqual(res.rcri["classe_risco"], "alto")
        # Estresse condicionado ao N8
        self.assertIn("imagem_estresse", res.exames)
        self.assertEqual(res.exames["imagem_estresse"]["recomendacao"], "considerar")
        # RCRI ≥ 3 + METs ruim → discutir alternativas (N10)
        ids = [s["id"] for s in res.sinalizadores]
        self.assertIn("discutir_alternativas", ids)
        self.assertIn("N10", res.trajeto)

    def test_excecao_esc_45_anos_porte_alto_sem_fatores(self):
        respostas = dict(BASE_SAUDAVEL, ecg_12m=False, anticoagulante=False,
                         sopro_com_sintoma=False, sinais_ic=False)
        res = self.executa(idade=50, procedimento="pancreatectomia", **respostas)
        self.assertEqual(res.saida, "plano")
        self.assertEqual(res.porte, "alto")
        # Sem fatores de risco: pacote vira 'considerar' pela exceção ESC
        self.assertEqual(res.exames["ecg_repouso"]["recomendacao"], "considerar")
        self.assertEqual(res.exames["nt_probnp_bnp"]["recomendacao"], "considerar")
        self.assertTrue(any("Exceção ESC" in n for n in res.notas))

    def test_fragilidade_avancada_dispara_alternativas(self):
        respostas = dict(
            BASE_SAUDAVEL, hipertensao="bem_controlada",
            frail_score=4, mets_4="nao_sei",
            ecg_12m=True, anticoagulante=False,
            sopro_com_sintoma=False, sinais_ic=False,
        )
        res = self.executa(idade=80, procedimento="artroplastia de quadril", **respostas)
        self.assertEqual(res.saida, "plano")
        ids = [s["id"] for s in res.sinalizadores]
        self.assertIn("fragilidade", ids)
        self.assertIn("discutir_alternativas", ids)
        self.assertIn("N10", res.trajeto)

    def test_vigilancia_mins_desativavel(self):
        motor = Motor(config={"vigilancia_mins_ativa": False})
        respostas = dict(
            BASE_SAUDAVEL, hipertensao="mal_controlada",
            frail_score=1, mets_4="sim",
            ecg_12m=True, anticoagulante=False,
            sopro_com_sintoma=False, sinais_ic=False,
        )
        res = executar_cenario(motor, dict(respostas, idade=70, procedimento="colecistectomia"))
        self.assertEqual(res.saida, "plano")
        self.assertNotIn("hs_ctn_basal", res.exames)
        self.assertEqual(res.exames["nt_probnp_bnp"]["recomendacao"], "sim")

    # ---------------- Perguntas dinâmicas ----------------
    def test_fluxo_pergunta_a_pergunta(self):
        sessao = Sessao()
        passo = self.motor.avaliar(sessao)
        self.assertEqual(passo.id, "idade")
        sessao.responder("idade", 30)
        passo = self.motor.avaliar(sessao)
        self.assertEqual(passo.id, "cirurgia_eletiva")
        sessao.responder("cirurgia_eletiva", True)
        passo = self.motor.avaliar(sessao)
        self.assertEqual(passo.no, "N1")

    def test_porte_perguntado_quando_nao_reconhecido(self):
        sessao = Sessao()
        for k, v in dict(BASE_SAUDAVEL, idade=30, procedimento="procedimento xyz").items():
            sessao.respostas[k] = v
        passo = self.motor.avaliar(sessao)
        self.assertEqual(passo.id, "porte")
        sessao.responder("porte", "baixo")
        res = self.motor.avaliar(sessao)
        self.assertIsInstance(res, Resultado)
        self.assertEqual(res.porte, "baixo")


if __name__ == "__main__":
    unittest.main()
