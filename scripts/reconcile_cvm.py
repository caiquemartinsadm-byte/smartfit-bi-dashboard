"""Conciliação independente dos ZIPs oficiais da CVM. Python 3, sem dependências.
Uso: python scripts/reconcile_cvm.py --raw-dir data/raw/cvm
Use --download para baixar os ZIPs públicos (requer internet).
Não modifica index.html. Gera proposta e diferenças para revisão.
"""
import argparse, csv, io, json, re, urllib.request, zipfile
from decimal import Decimal
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = "https://dados.cvm.gov.br/dados/CIA_ABERTA/DOC/"
ACCOUNTS = {"receita_ri":"3.01","custos_ri":"3.02","bruto_ri":"3.03",
            "despesas_total":"3.04","equiv_ri":"3.04.06","operacional_ri":"3.05",
            "financeiro_ri":"3.06","tributos_ri":"3.08","descontinuadas":"3.10",
            "lucro_ri":"3.11"}
def url(kind, year):
    return f"{BASE}{kind}/DADOS/{kind.lower()}_cia_aberta_{year}.zip"

def load(kind, year, directory, download):
    stem=f"{kind.lower()}_cia_aberta_{year}"
    path=directory/(stem+".zip")
    if download and not path.exists():
        urllib.request.urlretrieve(url(kind,year),path)
    if not path.exists():
        raise FileNotFoundError(path)
    member=f"{kind.lower()}_cia_aberta_DRE_con_{year}.csv"
    with zipfile.ZipFile(path) as z:
        with z.open(member) as f:
            reader=csv.DictReader(io.TextIOWrapper(f,encoding="latin-1"),delimiter=";")
            rows=[r for r in reader if r["CD_CVM"].lstrip("0")=="24260" and
                  r["ORDEM_EXERC"]=="ÚLTIMO"]
    return rows,member

def period(rows, start, end):
    # Choose latest document version globally for this reference date.
    ref=[r for r in rows if r["DT_REFER"]==end]
    version=max(int(r["VERSAO"]) for r in ref)
    chosen=[r for r in ref if int(r["VERSAO"])==version and r["DT_INI_EXERC"]==start
            and r["DT_FIM_EXERC"]==end]
    values={}
    for field, code in ACCOUNTS.items():
        matches=[r for r in chosen if r["CD_CONTA"]==code]
        if len(matches)!=1:
            raise ValueError(f"{end} V{version}: conta {code}, {len(matches)} registros")
        r=matches[0]
        multiplier={"MIL":Decimal(1000),"UNIDADE":Decimal(1)}[r["ESCALA_MOEDA"]]
        if r["MOEDA"]!="REAL":
            raise ValueError("Moeda não suportada: "+r["MOEDA"])
        values[field]=Decimal(r["VL_CONTA"].replace(",","."))*multiplier
    return values,version

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--raw-dir",type=Path,default=ROOT/"data/raw/cvm")
    p.add_argument("--download",action="store_true")
    args=p.parse_args()
    args.raw_dir.mkdir(parents=True,exist_ok=True)
    html=(ROOT/"index.html").read_text(encoding="utf-8")
    rows=json.loads(re.search(r"const data=(\[.*?\]); const visible",html,re.S).group(1))
    report=[]
    proposals=[]
    for y in range(2022,2027):
        itr,im=load("ITR",y,args.raw_dir,args.download)
        for q,(start,end) in enumerate([("01-01","03-31"),("04-01","06-30"),
                                      ("07-01","09-30"),("10-01","12-31")],1):
            if y==2026 and q==4: break
            if q<4:
                v,version=period(itr,f"{y}-{start}",f"{y}-{end}")
                source=f"{url('ITR',y)} | {im} | V{version} | {y}-{start} a {y}-{end}"
            else:
                dfp,dm=load("DFP",y,args.raw_dir,args.download)
                annual,dv=period(dfp,f"{y}-01-01",f"{y}-12-31")
                nine,nv=period(itr,f"{y}-01-01",f"{y}-09-30")
                v={k:annual[k]-nine[k] for k in annual}
                source=f"{url('DFP',y)} | {dm} V{dv} menos {url('ITR',y)} | {im} V{nv} 9M"
            if v["descontinuadas"]!=0:
                raise ValueError(f"{y}Q{q}: revisar operações descontinuadas")
            v["despesas_ri"]=v["despesas_total"]-v["equiv_ri"]
            # Exact reported subtotals must close. No artificial balancing item.
            if (v["receita_ri"]+v["custos_ri"]!=v["bruto_ri"] or
                v["bruto_ri"]+v["despesas_total"]!=v["operacional_ri"] or
                v["operacional_ri"]+v["financeiro_ri"]+v["tributos_ri"]!=v["lucro_ri"]):
                raise ValueError(f"{y}Q{q}: DRE não fecha; revisar fonte")
            old=next(r for r in rows if int(r["ano"])==y and int(r["trimestre"])==q)
            proposal={"periodo":old["periodo"]}
            for field in ["receita_ri","custos_ri","bruto_ri","despesas_ri","equiv_ri",
                          "operacional_ri","financeiro_ri","tributos_ri","lucro_ri"]:
                previous=Decimal(str(old[field]))*1000000
                proposal[field.replace("_ri","_dre_brl")]=str(v[field])
                account="3.04 menos 3.04.06" if field=="despesas_ri" else ACCOUNTS[field]
                report.append({"periodo":old["periodo"],"campo":field,"conta":account,
                               "v5_ri_brl":str(previous),"cvm_brl":str(v[field]),
                               "delta_cvm_menos_v5_brl":str(v[field]-previous),"fonte":source})
            for k,field in [("receita_mil_brl","receita_ri"),("lucro_mil_brl","lucro_ri")]:
                if Decimal(str(old[k]))*1000!=v[field]:
                    print("DIVERGÊNCIA KPI PRINCIPAL:",old["periodo"],k,old[k],v[field]/1000)
            proposals.append(proposal)
    out=ROOT/"docs/evidencias"
    out.mkdir(parents=True,exist_ok=True)
    for name, data in [("cvm_conciliacao_exata.csv",report),("cvm_dre_proposta.csv",proposals)]:
        with (out/name).open("w",encoding="utf-8",newline="") as f:
            w=csv.DictWriter(f,fieldnames=list(data[0]))
            w.writeheader()
            w.writerows(data)
    print(f"{len(proposals)} trimestres e {len(report)} comparações; revisar antes de alterar o painel.")

if __name__=="__main__":
    main()
