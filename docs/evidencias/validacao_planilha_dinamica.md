# Validação da Planilha Dinâmica 3T26

Arquivo fornecido pelo usuário: Planilha Dinâmica 3T26.xlsx.
Fonte declarada: [RI Smart Fit — Planilha Dinâmica](https://investor.smartfit.com.br/informacoes-financeiras/planilha-dinamica/).
SHA-256 do arquivo recebido: `c6b854c6296a9ce5918f16c73f882ec69aa9b056b85ea2b73bfeef76a8ef0779`.

Foram lidos os valores armazenados nas células do XLSX (incluindo valores em cache de fórmulas, sem recalcular a planilha) e comparados ao HTML V5. Os 19 trimestres são identificados pelos cabeçalhos, de R a AJ. A matriz [matriz_planilha_dinamica.csv](matriz_planilha_dinamica.csv) contém 323 comparações, todas coincidentes (114 operacionais e 209 financeiras RI). Para a série de clientes em milhares, multiplicação por 1.000 e arredondamento à unidade; para os valores financeiros em milhões, tolerância absoluta de 1e-9 milhão para diferenças de ponto flutuante. Nenhum valor foi alterado.

## Mapeamento das células

- Indic. Operac., linhas 3, 5 e 6: academias totais, próprias, franquias.
- Indic. Operac., linhas 29, 31 e 32: clientes de academias, próprias, franquias, em milhares.
- DRE Contábil, linhas 2, 3, 4, 7, 10, 17, 19, 21, 22, 24 e 28: receita bruta, líquida, custos, lucro bruto, despesas, equivalência, resultado operacional, financeiro, tributos, lucro líquido e EBITDA, em R$ milhões.

## Escopo e comparabilidade

Aba Indic. Operac., A47:A55: posição de fim de período; clientes B2C, não incluem usuários de agregadores no Brasil e México, nem alunos TotalPass; academias excluem studios; clientes digitais já contabilizados em academias ou studios não são contados novamente. As linhas totais de academias incluem marcas do grupo, não apenas Smart Fit. Evolve (30 academias) e seus clientes foram integrados em agosto de 2026. A nota A52 também registra a conversão da academia O2 em Bio Ritmo em 2025.

Aba DRE Contábil, A31:A32: consolidação de Panamá e Costa Rica no 1T23, Velocity ao final de 2024, Fitmaster a partir de 2T25, TotalPass México a partir de 1T26 e Evolve a partir de agosto de 2026. Despesas incluem depreciação/amortização e gastos pré-operacionais. Crescimento consolidado não equivale a crescimento orgânico.

## Limite da conclusão

A série RI da V5 foi reproduzida integralmente. Isso não elimina as pequenas diferenças em relação à DRE das demonstrações oficiais, já registradas em conciliacao_ri_dre.csv. A conciliação exata de todas as contas da CVM continua pendente. A planilha recebida não substitui os ITRs/DFPs. Nenhum dado ou layout do dashboard foi alterado; o arquivo Excel original não foi republicado.
