"""Extrai os dados incorporados ao dashboard V5. Não coleta dados das fontes oficiais."""
import csv, json, re, calendar
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
html = (ROOT / "index.html").read_text(encoding="utf-8")
match = re.search(r"const data=(\[.*?\]); const visible", html, re.S)
if not match:
    raise ValueError("Base incorporada não encontrada.")
rows = json.loads(match.group(1))
out = ROOT / "data" / "processed"
out.mkdir(parents=True, exist_ok=True)
with (out / "dashboard_data.csv").open("w", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=list(rows[0]), lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
with (out / "financial_data.csv").open("w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f, lineterminator="\n")
    writer.writerow(["period", "reference_date", "net_revenue_brl", "net_income_brl"])
    for r in rows:
        y, q = int(r["ano"]), int(r["trimestre"])
        m = q * 3
        writer.writerow([f"{y}Q{q}", f"{y}-{m:02d}-{calendar.monthrange(y,m)[1]:02d}",
                         int(r["receita_mil_brl"] * 1000), int(r["lucro_mil_brl"] * 1000)])
