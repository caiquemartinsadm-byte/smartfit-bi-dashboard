# Smart Fit | Business Intelligence & Analytics

Projeto independente de portfólio que investiga se a expansão da rede Smart Fit está acompanhada de crescimento rentável.

## Dashboard

A versão V5 reúne três páginas: Visão executiva, Expansão da rede e Rentabilidade. A base inclui 19 trimestres (1T22 a 3T26); a interface apresenta 15 (1T23 a 3T26), usando 2022 como referência para comparações anuais.

Para explorar o painel, abra `index.html` em um navegador. O arquivo é autônomo, construído em HTML, CSS, JavaScript e SVG, sem dependências externas. Para hospedar, pode-se utilizar GitHub Pages a partir da raiz do repositório.

## Dados e metodologia

- Visão executiva: receita líquida, lucro líquido consolidado, margem líquida e variações anuais, identificados no painel como dados da DRE consolidada da CVM.
- Expansão: academias e clientes de academias, separados entre próprias e franquias; dados identificados como provenientes da Planilha Dinâmica de RI.
- Rentabilidade: cascata da DRE e margens bruta, operacional e EBITDA da série contábil de RI; a margem líquida da CVM permanece separada.
- Ticket médio não apresentado por ausência de série comparável. Valores ausentes não são tratados como zero.

## Reprodução

1. Baixe ou clone o repositório.
2. Abra `index.html` para utilizar o dashboard.
3. Opcionalmente, execute `python scripts/extract_dashboard_data.py` com Python 3 para reproduzir os CSVs a partir da base incorporada ao HTML.
4. Consulte [o dicionário de dados](docs/data_dictionary.md) e [o registro de validação](docs/validation.md).

A extração reproduz a base do painel, não a coleta original na CVM ou no RI.

## Fontes e status

Fontes declaradas na V5: [CVM](https://dados.cvm.gov.br/) e [Relações com Investidores da Smart Fit](https://investor.smartfit.com.br/). O painel V5 foi aprovado para apresentação. A revisão de 152 observações dos indicadores básicos consta em [docs/evidencias/RELATORIO.md](docs/evidencias/RELATORIO.md): 95 coincidências exatas e 57 na precisão publicada. A Planilha Dinâmica 3T26 foi conferida em 323 observações (114 operacionais e 209 financeiras RI), todas coincidentes com a V5; veja [as evidências por célula](docs/evidencias/validacao_planilha_dinamica.md). A validação direta dos ZIPs da CVM e a conciliação integral entre a DRE da CVM e a série RI ainda estão pendentes. Consulte [o registro atualizado](docs/validation.md).

## Uso de inteligência artificial

O projeto foi desenvolvido com apoio de IA generativa na pesquisa, organização e tratamento dos dados, programação e documentação. A interpretação dos resultados e a revisão das fontes fazem parte do processo de avaliação do projeto.

Projeto educacional e de portfólio, sem vínculo institucional com a Smart Fit.
