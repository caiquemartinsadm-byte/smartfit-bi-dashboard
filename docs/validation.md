# Validação final — V5 conciliada

Revisão aprovada pelo responsável pelo projeto. Base: 1T22–3T26.

- CVM: 19/19 trimestres, 38/38 coincidências exatas de receita e lucro, 171 comparações de componentes da DRE e fechamento de 19 cascatas.
- RI: 323/323 observações conferidas contra a Planilha Dinâmica 3T26; 114 operacionais e 209 financeiras.
- 4T: DFP anual menos ITR de nove meses. DFP 2022 V2; demais DFPs V1. ITR 2T26 V2.
- A causa das diferenças entre CVM e RI não foi confirmada. Os valores originais RI foram preservados; a cascata usa os valores CVM.
- Verificação da versão publicada: 19 registros, colunas originais intactas, CSS idêntico, fechamento aritmético e igualdade dos KPIs CVM. Não foi realizado teste visual em navegador nesta etapa.

## Evidências

- [Conciliação completa CVM](evidencias/conciliacao_cvm_completa.csv)
- [Memória de cálculo 4T](evidencias/memoria_calculo_4t_cvm.csv)
- [Planilha Dinâmica: células e escopo](evidencias/validacao_planilha_dinamica.md)
- [Matriz RI](evidencias/matriz_planilha_dinamica.csv)
- [Revisão anterior](evidencias/RELATORIO.md)

Os ZIPs e XLSX originais não são republicados. As evidências incluem a localização e identificação das fontes. O script de extração reproduz a base incorporada; a rotina independente reconcile_cvm.py foi criada na revisão anterior e não é certificada como reproduzível nesta etapa.
