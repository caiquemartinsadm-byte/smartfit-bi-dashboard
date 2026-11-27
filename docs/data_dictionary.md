# Dicionário de dados

Definições recuperadas da interface V5; a documentação original das fontes não foi fornecida.

| Campos | Definição | Unidade |
|---|---|---|
| periodo; ano; trimestre; exibir | Identificação temporal; exibir indica os períodos visíveis na interface. | rótulo; ano; trimestre; booleano |
| receita_mil_brl; lucro_mil_brl | Receita líquida e lucro líquido consolidado, atribuídos à CVM no painel. | R$ mil |
| academias; academias_proprias; academias_franquias | Total, próprias e franquias, fim do trimestre, atribuídos ao RI. | unidades |
| clientes_academias; clientes_proprias; clientes_franquias | Clientes B2C de academias, fim do trimestre; exclui TotalPass, estúdios e digital conforme painel. | clientes |
| margem_liquida_pct | 100 × lucro / receita (série CVM). | % |
| receita_mil_brl_yoy_pct; academias_yoy_pct; clientes_academias_yoy_pct; lucro_mil_brl_yoy_pct | Variação contra o mesmo trimestre anterior (ano anterior). Lucro ausente quando a base anterior é negativa. | % |
| lucro_variacao_mil_brl | Lucro atual menos lucro do mesmo trimestre do ano anterior. | R$ mil |
| margem_variacao_pp | Margem atual menos margem do mesmo trimestre do ano anterior. | p.p. |
| ticket_medio | Ausente em todos os períodos; não exibido. | não definida |
| receita_ri; custos_ri; bruto_ri; despesas_ri; equiv_ri; operacional_ri; financeiro_ri; tributos_ri; lucro_ri | Componentes da DRE contábil atribuída ao RI no painel. | R$ milhões |
| ebitda_ri; faturamento_ri | EBITDA identificado como contábil IFRS 16 e faturamento da série RI. | R$ milhões |

No CSV financeiro simplificado, `period` é AAAAQn, `reference_date` é a data de encerramento trimestral, e `net_revenue_brl` e `net_income_brl` estão em reais.
