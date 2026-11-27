# Smart Fit | Business Intelligence & Analytics

Projeto independente de portfólio que investiga se a expansão da rede Smart Fit está acompanhada de crescimento rentável.

## Dashboard

A versão V5 conciliada reúne três páginas: Visão executiva, Expansão da rede e Rentabilidade. A base inclui 19 trimestres (1T22 a 3T26); a interface apresenta 15 (1T23 a 3T26), usando 2022 como referência para comparações anuais.

Abra `index.html` em um navegador. O arquivo é autônomo, construído em HTML, CSS, JavaScript e SVG, sem dependências externas.

## Dados e metodologia

- Visão executiva: receita líquida, lucro líquido consolidado, margem líquida e variações anuais, provenientes da DRE consolidada da CVM.
- Expansão: academias e clientes de academias, separados entre próprias e franquias, provenientes da Planilha Dinâmica do RI.
- Rentabilidade: cascata da DRE e margens bruta, operacional e líquida da CVM; EBITDA, faturamento e respectiva receita permanecem na série RI.
- Ticket médio não apresentado por ausência de série comparável. Valores ausentes não são tratados como zero.

## Validação

Os 19 trimestres foram conferidos nos ITRs e DFPs recebidos da CVM, com 38 coincidências exatas de receita e lucro. A conciliação dos nove componentes da DRE gerou 171 comparações. A Planilha Dinâmica 3T26 foi conferida em 323 observações, todas coincidentes com a série RI original. A cascata utiliza exclusivamente os valores CVM, preservando a série RI em colunas separadas. A causa das diferenças entre fontes não foi confirmada.

Consulte [o registro de validação](docs/validation.md), [o dicionário de dados](docs/data_dictionary.md) e [as evidências](docs/evidencias/).

## Reprodução

1. Baixe ou clone o repositório.
2. Abra `index.html` no navegador.
3. Execute `python scripts/extract_dashboard_data.py` com Python 3 para reproduzir os CSVs a partir da base incorporada ao HTML.
4. Para conferir a origem contábil, utilize os arquivos ITR 2022–2026 e DFP 2022–2025 disponíveis no portal da CVM e os registros de contas, versões e hashes em `docs/evidencias`. A extração do HTML não equivale à coleta independente.

Fontes: [CVM](https://dados.cvm.gov.br/) e [Relações com Investidores da Smart Fit](https://investor.smartfit.com.br/).

## Uso de inteligência artificial

O projeto foi desenvolvido com apoio de IA generativa na pesquisa, tratamento dos dados, programação e documentação, com revisão e aprovação do responsável pelo portfólio.

Projeto educacional e de portfólio, sem vínculo institucional com a Smart Fit.
