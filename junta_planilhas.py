import glob
import os
import pandas as pd

arquivos = sorted(glob.glob(os.path.join("planilhas", "*.xlsx")))
if not arquivos:
    raise SystemExit("Nenhuma planilha encontrada na pasta 'planilhas'.")

colunas_padrao = None
tabelas = []

for arq in arquivos:
    df = pd.read_excel(arq)
    df.columns = df.columns.str.strip().str.lower()
    nome = os.path.basename(arq)

    if colunas_padrao is None:
        colunas_padrao = list(df.columns)
    elif list(df.columns) != colunas_padrao:
        print(f"Aviso: {nome} tem colunas diferentes {list(df.columns)} e foi ignorada.")
        continue

    df["arquivo_origem"] = nome
    tabelas.append(df)

total = pd.concat(tabelas, ignore_index=True)
linhas_antes = len(total)
total = total.drop_duplicates(subset=colunas_padrao)

print(f"Arquivos lidos: {len(tabelas)} de {len(arquivos)}")
print(f"Linhas antes: {linhas_antes} | depois: {len(total)} | duplicadas removidas: {linhas_antes - len(total)}")

os.makedirs("saida", exist_ok=True)
total.to_excel(os.path.join("saida", "planilha_unificada.xlsx"), index=False)
print("Arquivo salvo em saida/planilha_unificada.xlsx")