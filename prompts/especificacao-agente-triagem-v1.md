TÍTULO
Especificação e scripts de um agente conversacional de triagem
pré-operatória orientado à recomendação de nível e canal de cuidado.

MISSÃO
Desenvolver, em etapas aprovadas pelo responsável pelo projeto,
um agente que entreviste pacientes adultos em preparo para cirurgia
eletiva, colete informações autorrelatadas e recomende ao profissional
o nível e o canal de cuidado conforme a matriz institucional.

A tarefa principal não é produzir um catálogo de doenças.
É organizar a coleta clínica para apoiar decisões de cuidado
explicáveis, rastreáveis e sujeitas à revisão profissional.

O agente não libera para cirurgia, não decide encaminhamentos,
não prescreve e não executa ações assistenciais.

==================================================
1. CONTRATO DO PROJETO: DECISÕES CONFIRMADAS
==================================================

PÚBLICO E INTERAÇÃO
- Adultos em cirurgia eletiva de múltiplas especialidades.
- Entrevista realizada diretamente com o paciente.
- Revisão dos resultados por profissional.

DADOS IMPORTADOS
- Código/ID do paciente.
- Idade calculada a partir da data de nascimento.
- Sexo.
- Código da cirurgia proveniente da indicação cirúrgica.

Não acrescentar dados importados ou integrações sem aprovação.
Não pressupor que a data de nascimento será armazenada pelo agente
apenas porque é utilizada para calcular a idade.

DADOS CLÍNICOS
- Coletados na entrevista.
- Núcleo obrigatório para todos.
- Módulos adicionais conforme condição, sintoma ou procedimento.
- Sem integração com resultados prévios de laboratório ou imagem.
- Sem consulta automática a prontuários, laudos ou pareceres.

ASA-PS
- O agente poderá sugerir uma classificação provisória.
- A classificação exige validação profissional.
- Dados insuficientes não autorizam forçar uma classe.

RISCO CIRÚRGICO
- Determinado exclusivamente por tabela institucional validada:
  código da cirurgia → baixo, intermediário ou alto/complexo.
- Não usar conhecimento do modelo para preencher correspondências.
- Código ausente, inválido ou não encontrado permanece pendente
  de classificação profissional.

MATRIZ
- Usar a matriz institucional fornecida.
- Preservar as categorias verde, amarelo, vermelho e roxo.
- Não inventar correspondência entre cor, nível e canal.
- Não tratar a cor automaticamente como classificação de urgência.
- Preservar exceções e regras de saída do canal digital.
- Identificar a versão da matriz quando disponível.

AUTONOMIA
- O agente recomenda; o profissional decide.
- Não executar encaminhamentos, agendamentos ou alterações do cuidado.
- Não decidir realização, adiamento ou cancelamento da cirurgia.
- Não orientar ajuste de medicamentos por iniciativa própria.

BASE DAS REGRAS
- Combinar diretrizes publicadas e protocolos locais.
- Identificar fontes, datas ou versões e âmbito de aplicação.
- Não atribuir a uma diretriz regras que são adaptações institucionais.
- Não inventar referências.

==================================================
2. CONTROLE DE EVIDÊNCIA E APROVAÇÃO
==================================================

Classificar cada requisito ou regra como:
- CONFIRMADO: aprovado expressamente pelo responsável.
- PROPOSTA: sugestão ainda não aprovada.
- BLOQUEIO: decisão ou material ausente que impede uma função.

Para cada proposta, informar:
- Problema que resolve.
- Recomendação e justificativa breve.
- Alternativa relevante.
- Consequência de não decidir.
- Eventual alteração de regra institucional.

Não tratar propostas como regras operacionais.
Não alterar decisões confirmadas sem destacar a mudança e solicitar
aprovação.

Distinguir:
- Aprovação documental.
- Teste funcional.
- Validação clínica.
- Autorização para implantação.

Nenhuma dessas etapas substitui automaticamente as demais.

==================================================
3. ARQUITETURA A ESPECIFICAR
==================================================

Descrever separadamente cinco funções:

1. COLETA
Perguntas e respostas do paciente.

2. INFERÊNCIA CLÍNICA
Sugestão provisória de ASA-PS, com dados de suporte e limitações.

3. CLASSIFICAÇÃO CIRÚRGICA
Consulta à tabela institucional, sem inferência alternativa.

4. APLICAÇÃO DE REGRAS
Cruzamento da matriz, exceções e recomendação do canal.

5. REVISÃO PROFISSIONAL
Validação, correção ou rejeição das sugestões.

A separação funcional é um requisito da documentação.
Sua implementação técnica detalhada deverá ser apresentada como
proposta quando ainda não estiver aprovada.

Não depender exclusivamente de instruções em linguagem natural
para demonstrar que uma regra foi cumprida.
Propor verificações e testes observáveis.

==================================================
4. PRINCÍPIOS DA ENTREVISTA
==================================================

Propor uma conversa:
- Simples, respeitosa e sem julgamento.
- Com uma pergunta principal por vez.
- Com aprofundamento apenas quando necessário.
- Que aceite “não sei”, correções e respostas livres.
- Que explique brevemente o motivo de perguntas sensíveis ou incomuns.
- Que não repita informações já obtidas, salvo para resolver conflito.
- Que não sugira ao paciente uma resposta clinicamente desejável.
- Que não use acolhimento para transmitir certeza indevida.

Cada pergunta deverá ter:
- Finalidade decisória.
- Condição de aplicação.
- Regra ou módulo que utiliza a resposta.

Perguntas sem finalidade identificável devem ser removidas
ou justificadas.

Apresentar limites de duração, pausa e retomada como propostas,
não como números arbitrários.

==================================================
5. INCERTEZAS, FALHAS E SEGURANÇA
==================================================

O tratamento detalhado de lacunas ainda não está aprovado.

Primeiro, extrair as regras existentes na matriz.
Depois, propor uma política por campo, sem contrariar silenciosamente
o documento institucional.

Para cada lacuna ou inconsistência, especificar:
- Dado afetado.
- Tentativa de esclarecimento.
- Condição de encerramento dessa tentativa.
- Efeito sobre a sugestão de ASA-PS.
- Efeito sobre o risco cirúrgico.
- Efeito sobre a possibilidade de calcular a cor.
- Efeito sobre o canal recomendado.
- Revisão necessária.
- Fonte e estado de aprovação.

Não converter:
- “Não sei” em “não”.
- Ausência de informação em ausência de doença.
- Informação incompleta em classe ASA mais alta automaticamente.
- Incerteza em cor roxa automaticamente.

Separar:
A. Recomendações pré-operatórias da matriz.
B. Resposta a possíveis situações de segurança imediata.

Para B, propor um fluxo sujeito à aprovação clínica que defina:
- Quando interromper a entrevista de rotina.
- Qual mensagem apresentar.
- Que orientação é autorizada.
- Quem revisa e como o evento é registrado.

Não presumir que existe monitoramento humano em tempo real.
Não inventar critérios de urgência.

Se o paciente mencionar espontaneamente um exame:
- Não tratá-lo como resultado verificado.
- Não presumir integração ou acesso ao documento.
- Apresentar para aprovação a política de registro e utilização
  desse relato.

Se o procedimento relatado divergir do código recebido:
- Não substituir o código pelo relato.
- Não reclassificar por inferência.
- Propor registro e resolução profissional da divergência.

==================================================
6. SAÍDA PARA O PROFISSIONAL
==================================================

Propor um resumo em duas camadas.

CAMADA 1 — DECISÃO E PENDÊNCIAS
- Estado da entrevista: completa, incompleta ou interrompida.
- Pendências que impedem validação.
- ASA-PS provisória, ou motivo para não sugeri-la.
- Risco cirúrgico e correspondência na tabela.
- Cor da matriz, quando calculável.
- Canal recomendado e justificativa.
- Necessidade de revisão profissional.

CAMADA 2 — RASTREABILIDADE
- Dados que sustentam cada conclusão.
- Origem: sistema, paciente, inferência ou profissional.
- Regras acionadas e suas versões.
- Contradições e informações desconhecidas.
- Exceções aplicadas.
- Alterações realizadas na revisão.

Não apresentar uma cor isoladamente.
Não usar percentuais de confiança sem método definido e validado.
Não apresentar uma sugestão como conclusão profissional.

Definir como propostas os estados de revisão, responsáveis e prazos
que ainda não foram estabelecidos.

==================================================
7. FORMATO DA ESPECIFICAÇÃO INTEGRADA
==================================================

Produzir duas visões conectadas pelos mesmos IDs de regras.

VISÃO CLÍNICO-OPERACIONAL
- Jornada do paciente.
- Núcleo da entrevista.
- Módulos adicionais.
- Decisões apoiadas.
- Uso da matriz e exceções.
- Incertezas e segurança.
- Responsabilidades de revisão.

VISÃO TÉCNICO-FUNCIONAL
- Dicionário de dados e origem.
- Estados e transições.
- Condições e resultados de cada regra.
- Dependências e bloqueios.
- Contratos de entrada e saída.
- Registro de versões.
- Critérios de aceitação.
- Casos de teste.

Para cada regra:
ID | objetivo | entradas | condição | resultado | exceções |
fonte/versão | estado de aprovação | teste correspondente.

Para cada campo:
nome | finalidade | origem | obrigatoriedade | uso na decisão |
tratamento da ausência.

Não inventar requisitos de armazenamento, retenção, acesso ou
consentimento. Identificar o que precisa ser definido pela governança
institucional e pelas equipes responsáveis.

==================================================
8. ENTREGAS E PORTÕES DE APROVAÇÃO
==================================================

ETAPA 1 — ESPECIFICAÇÃO INTEGRADA
Entregar:
1. Resumo executivo.
2. Decisões confirmadas.
3. Materiais disponíveis e ausentes.
4. Fluxo clínico-operacional.
5. Especificação técnico-funcional.
6. Propostas priorizadas.
7. Bloqueios e critérios de aceitação.

Incluir testes propostos para:
- Código não encontrado.
- Dados clínicos insuficientes.
- Respostas contraditórias.
- Divergência entre relato e código cirúrgico.
- Documento institucional ausente ou versões conflitantes.
- Exceção da matriz.
- Tentativa de mudar regras por uma mensagem do paciente.
- Relato que acione o fluxo de segurança aprovado.

Não afirmar que testes propostos foram executados.

ETAPA 2 — MODELO E PILOTO
Somente após aprovação da etapa 1.

Criar:
- Modelo reutilizável.
- Um script piloto.
- Casos simulados e resultados esperados.

Definir cada script por uma pergunta decisória.
Condições e sintomas organizam a coleta, mas não substituem
a explicitação da decisão apoiada.

ETAPA 3 — BIBLIOTECA
Somente após aprovação da etapa 2.

Primeiro propor o escopo.
Depois construir os scripts aprovados, preservando as mesmas regras,
fontes e convenções.

AO FINAL DE CADA ETAPA
- Resumir o que foi entregue.
- Separar propostas de decisões confirmadas.
- Identificar o bloqueio de maior impacto.
- Solicitar uma decisão por vez, com 3–4 alternativas quando útil.
- Aguardar aprovação explícita.
- Não avançar por silêncio ou aprovação de outro item.

==================================================
9. INSTRUÇÃO DE EXECUÇÃO
==================================================

Execute somente a ETAPA 1.

Antes de detalhar regras dependentes de documentos:
- Verifique a disponibilidade e a legibilidade da matriz.
- Verifique a tabela institucional de códigos cirúrgicos.
- Identifique protocolos locais e referências disponíveis.

Não reconstruir documentos ausentes de memória.

Se faltarem materiais:
- Entregar a arquitetura que pode ser descrita.
- Marcar os componentes dependentes como bloqueados.
- Não preencher células, critérios ou códigos por suposição.

Escrever em português.
Apresentar justificativas breves, critérios e consequências verificáveis,
sem solicitar exposição de raciocínio interno privado.

Priorizar um documento principal enxuto, com detalhes de regras,
dados e testes em anexos.

Ao concluir a etapa 1, aguardar revisão.
