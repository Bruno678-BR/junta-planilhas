import os
import random
import pandas as pd

os.makedirs("planilhas", exist_ok=True)
random.seed(1)

precos = {"Caneta": 3.5, "Caderno": 18.9, "Mochila": 89.9, "Lapis": 2.0, "Borracha": 1.5}

for i in range(1, 6):
    linhas = []
    for _ in range(20):
        produto = random.choice(list(precos))
        qtd = random.randint(1, 10)
        linhas.append({
            "data": f"2026-0{i}-{random.randint(1, 28):02d}",
            "produto": produto,
            "quantidade": qtd,
            "valor": round(qtd * precos[produto], 2),
        })
    df = pd.DataFrame(linhas)
    df = pd.concat([df, df.head(2)])  # duplicados de propósito
    if i == 5:
        df = df.rename(columns={"valor": "valor_total"})
    df.to_excel(f"planilhas/loja_{i}.xlsx", index=False)

print("Planilhas criadas.")