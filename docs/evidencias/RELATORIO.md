# Smart Fit — revisão de evidências da V5

Data: 27/11/2026. Status: revisão para aprovação; não é auditoria independente.

## Resultado

Foram comparados 19 trimestres (1T22–3T26) para oito indicadores básicos: 152 observações. As 38 observações financeiras e as 57 de quantidade de academias coincidem exatamente com as fontes consultadas; as 57 de clientes coincidem na precisão publicada (milhares). Os números de clientes unitários não foram comprovados. A fonte financeira efetivamente consultada foi a DRE consolidada das demonstrações oficiais publicadas pelo RI, não os CSVs originais da CVM. Os códigos 3.01 e 3.11 indicam o mapeamento de contas a conferir na CVM; a localização efetivamente consultada é a DRE, página 5 das demonstrações.

## Método

- Receita líquida e lucro líquido consolidado, em R$ mil, incluindo participações não controladoras; valores trimestrais ou comparativos do mesmo trimestre. 1T22 = 6M22 menos 2T22. O quarto trimestre = ano menos 9M, usando a DFP e o ITR. A DRE contábil dos releases 4T23 (p. 29) e 4T25 (p. 40) também confirma os quatro resultados na precisão de R$ 0,1 milhão.
- Academias: grupo, total/próprias/franquias, posição de fechamento. Clientes: clientes de academias, não clientes totais do grupo ou TotalPass; total/próprias/franquias. Comparação com a tabela dos releases em milhares, arredondando cada série independentemente. Não se exige que a soma de valores arredondados seja igual ao total publicado.
- A matriz registra valores V5 e fonte, precisão, delta, documento, localização e URL. Os dados de referência foram transcritos das tabelas; não são uma cópia dos valores V5.
- `conciliacao_ri_dre.csv` compara receita e lucro da série RI incorporada ao HTML com a DRE contábil oficial, em reais. Diferenças não justificam presumir erro de origem, mas exigem reconciliação.

## Divergências e recomendações

1. No 4T25, a receita RI do HTML é R$ 1.948.193.643,91 contra R$ 1.948.225.000 na DRE (delta -R$ 31.356,09). O lucro RI é R$ 214.434.156,06 contra R$ 214.430.000 (delta +R$ 4.156,06). Ambas as diferenças ficam abaixo da precisão de uma casa decimal em milhões do release. Entretanto, o lucro antes do resultado financeiro da V5 (R$ 456,745 milhões, arredondado para 456,7) não coincide com o release 4T25, p. 40 (456,8). Recomenda-se substituir a cascata contábil pela DRE reconciliada em todos os períodos, após aprovação e validação de todas as contas. Não alterar isoladamente os totais sem recalcular os componentes.
2. 1T23: consolidação de Panamá e Costa Rica a partir de 2023; 2T23: ganho de reavaliação de R$ 176,6 milhões; 4T23: efeito de imposto diferido de R$ 483 milhões (release 4T23, pp. 1, 5, 28–29). Não atribuir crescimento ou lucro integralmente à expansão orgânica.
3. 3T26: aquisição da Evolve em agosto de 2026, com 30 academias; separar efeito de perímetro de crescimento orgânico (release 3T26).
4. Manter ticket médio ausente até validar série comparável; não calcular receita do grupo dividida por clientes de academias como substituto.

## Pendências / limites

O ambiente não permitiu acessar o conteúdo tabular dos ZIPs originais da CVM nem da Planilha Dinâmica do RI. Os links estão no registro de fontes. Falta comprovar os números unitários de clientes, aba/célula, versão e protocolo de cada ITR/DFP na CVM, e validar todos os componentes da DRE RI, EBITDA e faturamento dos 19 trimestres. A cascata não está integralmente validada externamente. Portanto, a revisão cobre 19/19 trimestres dos oito indicadores básicos, não todos os campos da V5. Não foram alterados os arquivos do dashboard nem publicada a versão definitiva.

## Arquivos

- matriz_evidencias.csv — 152 observações.
- validacao_quartos_trimestres.csv — oito cálculos anuais menos nove meses.
- conciliacao_ri_dre.csv — 38 comparações de séries financeiras.
- fontes.csv — documentos consultados e fontes tabulares pendentes.

CSV UTF-8 com BOM, separador ponto e vírgula. Valores de referência de clientes em milhares; diferenças são calculadas na precisão da fonte. Valores monetários de reconciliação em reais, conforme conversão das unidades declaradas no HTML.
