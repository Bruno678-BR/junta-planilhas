# Junta planilhas com Python e pandas

Script em Python que lê várias planilhas Excel com as mesmas colunas, junta tudo em uma tabela só e remove as linhas duplicadas. Se algum arquivo vier com colunas diferentes, o script avisa e deixa esse arquivo de fora.

## Problema que resolve

Quem recebe uma planilha por loja, por mês ou por vendedor costuma juntar tudo na mão, copiando e colando. Isso demora e deixa passar linhas repetidas. O script faz esse trabalho em segundos e mostra quantas linhas foram removidas.

## Como rodar

1. Coloque os arquivos `.xlsx` na pasta `planilhas/`.
2. Abra o terminal na pasta do projeto e rode `python junta_planilhas.py`.
3. Pegue o resultado em `saida/planilha_unificada.xlsx`.

Para testar sem dados reais, rode antes `python gerar_planilhas.py`, que cria cinco planilhas de exemplo com duplicados de propósito. A quinta tem uma coluna com nome diferente, para testar o aviso.

## O que o script faz

- Lê todos os `.xlsx` da pasta `planilhas/`.
- Padroniza os nomes das colunas (sem espaços nas pontas e em minúsculas).
- Usa as colunas do primeiro arquivo como padrão. Arquivos com colunas diferentes são avisados no terminal e ignorados.
- Junta tudo em uma tabela e remove duplicados exatos.
- Acrescenta a coluna `arquivo_origem`, que mostra de qual planilha veio cada linha.
- Salva o resultado em `saida/planilha_unificada.xlsx`.

## Resultado no teste

Com as planilhas de exemplo, o script leu 4 dos 5 arquivos (a `loja_5.xlsx` foi ignorada por ter a coluna `valor_total` no lugar de `valor`). Foram 88 linhas antes e 80 depois, com 8 duplicadas removidas.

## Limitações

- O primeiro arquivo, em ordem alfabética, define as colunas padrão. Se ele for o diferente, os outros é que serão ignorados.
- Só remove duplicados exatos, com todas as colunas iguais.
- Lê apenas arquivos `.xlsx`.

## Arquivos

- `junta_planilhas.py`: script principal.
- `gerar_planilhas.py`: gera as planilhas de exemplo.
- `planilhas/`: planilhas de exemplo.

## Ferramentas

Python, pandas, openpyxl.
