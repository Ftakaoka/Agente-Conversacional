"""Testes de cenário da travessia do grafo de hemostasia/PBM.

Cada teste corresponde a uma afirmação que será feita em público. Se um deles
quebrar, a afirmação mudou.
"""

import unittest

from motor_grafo import Grafo, navegar, explicar


def pares(vereditos):
    return {(v.intervencao, v.estudo) for v in vereditos}


def codigos(vereditos):
    return {(v.falhas[0][0], v.intervencao, v.estudo) for v in vereditos}


class TestIntegridade(unittest.TestCase):
    def setUp(self):
        self.g = Grafo()

    def test_toda_aresta_aponta_para_no_existente(self):
        g = self.g
        for a in g.sugere:
            self.assertIn(a["de"], g.achados)
            self.assertIn(a["para"], g.mecanismos)
        for a in g.corrige:
            self.assertIn(a["de"], g.intervencoes)
            self.assertIn(a["para"], g.mecanismos)
        for m in g.mediu:
            self.assertIn(m["estudo"], g.estudos)
            self.assertIn(m["desfecho"], g.desfechos)
        for c in g.custa:
            self.assertIn(c["intervencao"], g.intervencoes)
            self.assertIn(c["desfecho"], g.desfechos)
        for e in g.estudos.values():
            for t in e["testou"]:
                self.assertIn(t["intervencao"], g.intervencoes)
        for p in g.pacientes.values():
            for a in p["achados"]:
                self.assertIn(a, g.achados)

    def test_apenas_desfecho_duro_ou_adverso_chega_em_casa(self):
        """A regra estrutural da tese: substituto é beco sem saída."""
        for id_desfecho, _sinal in self.g.conta_para.items():
            self.assertNotEqual(self.g.desfechos[id_desfecho]["tipo"], "substituto")
        for d in self.g.desfechos.values():
            if d["tipo"] == "substituto":
                self.assertIsNone(self.g.chega_em_casa(d["id"]))

    def test_toda_aresta_de_evidencia_declara_seu_estado_de_auditoria(self):
        estados = {"confirmado", "corrigido", "nao_no_resumo"}
        for m in self.g.mediu:
            self.assertIn(m.get("verificacao"), estados,
                          f"{m['estudo']}/{m['desfecho']} sem estado de verificação")
            self.assertEqual(m["auditado"], m["verificacao"] in ("confirmado", "corrigido"),
                             f"{m['estudo']}/{m['desfecho']}: auditado incoerente com verificacao")

    def test_todo_estudo_indexavel_tem_pmid_e_doi(self):
        for e in self.g.estudos.values():
            if e["id"] == "PLASMA-PROFILATICO":
                continue          # corpo de revisões, sem artigo único indexado
            self.assertTrue(e.get("pmid"), f"{e['id']} sem PMID")
            self.assertTrue(e.get("doi"), f"{e['id']} sem DOI")

    def test_aresta_nao_verificada_nao_pontua(self):
        """Regra geral: o que não foi conferido não sustenta veredito."""
        naovalidadas = [m for m in self.g.mediu if m["verificacao"] == "nao_no_resumo"]
        self.assertTrue(naovalidadas, "o teste perde o sentido se não houver aresta pendente")
        for pid in self.g.pacientes:
            for v in navegar(self.g, pid)["sobreviventes"] + navegar(self.g, pid)["condicionais"]:
                for m in v.medidas_duras + v.medidas_substitutas:
                    self.assertNotEqual(m["verificacao"], "nao_no_resumo")

    def test_medida_direta_do_terminal_nao_e_substituto(self):
        d = self.g.desfechos["D_daoh30"]
        self.assertTrue(d["terminal_direto"])
        self.assertEqual(d["tipo"], "duro")
        self.assertEqual(self.g.chega_em_casa("D_daoh30"), "+")


class TestP1Ortopedico(unittest.TestCase):
    """Dona Cleusa — artroplastia eletiva, anêmica ferropriva."""

    def setUp(self):
        self.g = Grafo()
        self.r = navegar(self.g, "P1")

    def test_txa_sobrevive_pelo_poise3(self):
        self.assertIn(("I_txa", "POISE3-TXA"), pares(self.r["sobreviventes"]))

    def test_crash2_e_woman_vao_para_o_cemiterio_por_elegibilidade(self):
        """O ponto alto da aula: os ensaios mais famosos do TXA não são dela."""
        self.assertIn(("F1", "I_txa", "CRASH-2"), codigos(self.r["cemiterio"]))
        self.assertIn(("F1", "I_txa", "WOMAN"), codigos(self.r["cemiterio"]))

    def test_plasma_profilatico_nao_tem_caminho_ate_casa(self):
        self.assertIn(("F2", "I_plasma", "PLASMA-PROFILATICO"), codigos(self.r["cemiterio"]))

    def test_ferro_ev_cai_por_medida_direta_do_no_terminal(self):
        """Lido o texto completo: o PREVENTT mediu DAOH-30 — o próprio nó CASA —
        e ficou plano (−0,1 dia; −1,5 a 1,2). Nenhum secundário sobrepõe isso."""
        self.assertIn(("F5", "I_ferro_ev", "PREVENTT"), codigos(self.r["cemiterio"]))

    def test_o_ganho_de_readmissao_do_ferro_vira_ressalva_de_horizonte(self):
        """O ganho existe e é pré-especificado — mas fora da janela de 30 dias.
        O grafo precisa dizer isso, não engolir."""
        v = next(x for x in self.r["cemiterio"]
                 if (x.intervencao, x.estudo) == ("I_ferro_ev", "PREVENTT"))
        self.assertTrue(any(r.startswith("HORIZONTE") for r in v.ressalvas))

    def test_estrategia_restritiva_sobrevive_por_nao_inferioridade(self):
        self.assertIn(("I_restritiva", "TRICS-III"), pares(self.r["sobreviventes"]))

    def test_mint_aparece_como_limite_e_nao_como_veredito(self):
        self.assertNotIn("MINT", {v.estudo for v in self.r["sobreviventes"] + self.r["cemiterio"]})
        self.assertTrue(any("MINT" in v.limites for v in self.r["sobreviventes"]))


class TestP3Cardiaco(unittest.TestCase):
    """Sra. Ivone — sangramento difuso pós-CEC com fibrinogênio baixo."""

    def setUp(self):
        self.g = Grafo()
        self.r = navegar(self.g, "P3")

    def test_concentrado_de_fibrinogenio_morre_no_desfecho_substituto(self):
        """FIBRES mediu unidades transfundidas. Não há aresta até CASA."""
        self.assertIn(("F2", "I_fibrinogenio", "FIBRES"), codigos(self.r["cemiterio"]))

    def test_crioprecipitado_empirico_e_inelegivel(self):
        self.assertIn(("F1", "I_crio", "CRYOSTAT-2"), codigos(self.r["cemiterio"]))

    def test_txa_cardiaco_e_condicional_nao_sobrevivente(self):
        """ATACAS: não-inferioridade em duro + ganho em substituto."""
        self.assertIn(("I_txa", "ATACAS"), pares(self.r["condicionais"]))


class TestF0(unittest.TestCase):
    def test_intervencao_sem_ensaio_recebe_lapide_propria(self):
        g = Grafo()
        r = navegar(g, "P2")
        sem_ensaio = {v.intervencao for v in r["cemiterio"] if v.falhas[0][0] == "F0"}
        self.assertIn("I_andexanet", sem_ensaio)
        self.assertIn("I_rfviia", sem_ensaio)


class TestExplicacao(unittest.TestCase):
    def test_toda_linha_do_trajeto_nomeia_uma_aresta_ou_marcador(self):
        g = Grafo()
        prefixos = ("APRESENTA", "SUGERE", "CORRIGE", "TESTOU", "ELEGIVEL", "MEDIU",
                    "CONTA_PARA", "CUSTA", "CONFLITA_COM", "JANELA", "LIMITE",
                    "   └─", "⚠", "⛔", "⚑", "Isto não prova")
        for pid in g.pacientes:
            r = navegar(g, pid)
            for grupo in ("sobreviventes", "condicionais", "cemiterio"):
                for v in r[grupo]:
                    _titulo, linhas = explicar(g, v)
                    for linha in linhas:
                        self.assertTrue(linha.startswith(prefixos),
                                        f"linha sem aresta correspondente: {linha!r}")


if __name__ == "__main__":
    unittest.main()
