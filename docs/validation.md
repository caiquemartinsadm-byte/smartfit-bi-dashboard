# Validação — situação da revisão em 27/11/2026

A revisão anterior está preservada em [evidencias/RELATORIO.md](evidencias/RELATORIO.md), acompanhada de matriz, fontes, conciliação e cálculo dos quartos trimestres.

## Evidências adicionais
- ITR de 30/06/2026 V2, protocolo 024260ITR300620260200160235-63, enviado em 06/08/2026: correção da apresentação de controladora/consolidado no formulário CVM, sem alteração do resultado ou patrimônio líquido. [Registro oficial](https://www.rad.cvm.gov.br/ENETWEB/frmGerenciaPaginaFRE.aspx?CodigoTipoInstituicao=1&NumeroSequencialDocumento=160235).
- Release 3T26, p. 12 (receita bruta), 37 (DRE reportada e EBITDA incluindo IFRS 16), 39 (DRE contábil): https://filemanager-cdn.mziq.com/published/757d3905-6a2d-496a-bbb0-32ddd17de6a0/17930d45-d74a-45bd-87e6-79fa10b347a6. A conferência adicional está em [conferencia_release_3T26.csv](evidencias/conferencia_release_3T26.csv). Despesas agregadas só foram comparadas quando o total foi publicado; traço em equivalência representa zero na tabela contábil, não preenchimento de dado ausente.
- Planilha Dinâmica: [página oficial](https://investor.smartfit.com.br/informacoes-financeiras/planilha-dinamica/) e [arquivo Excel](https://api.mziq.com/mzfilemanager/v2/d/757d3905-6a2d-496a-bbb0-32ddd17de6a0/b3fa8399-e11e-b82e-14e2-666ef41a1ca9?origin=2). A consulta retornou tipo XLSX não suportado; download também falhou.
- ZIP CVM retornou tipo ZIP não suportado; acesso direto no ambiente falhou. Não há validação exata dos arquivos originais nesta etapa.

## Próxima conciliação reproduzível
`python scripts/reconcile_cvm.py --download` em ambiente com internet, ou coloque os ZIPs de ITR 2022–2026 e DFP 2022–2025 em `data/raw/cvm` e execute `python scripts/reconcile_cvm.py`. A rotina proposta usa DRE consolidada, código CVM 24260, última versão e trimestre isolado; 4T por DFP menos 9M. Gera CSV de diferenças e proposta separada. Não executada com dados reais, pois os arquivos não estão disponíveis. Revisar eventuais exceções de conta/escala e reconciliar com as demonstrações antes de usar.

Não usar os valores arredondados do release como substituto de valores exatos. A validação de clientes até a unidade, a série completa de EBITDA/faturamento e a conciliação integral dos componentes da cascata permanecem pendentes. A versão HTML foi mantida intacta; não há alteração de valores sem comprovação. A publicação definitiva aguarda a resolução das pendências e revisão.
