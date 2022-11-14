import pandas as pd

url = "https://dedalo.sti.fab.mil.br/dadosabertos/fator_contribuinte.csv"
dados = pd.read_csv(url, sep=';', encoding='utf-8')

def fator(tipo):
    ocorrencia = dados.fator_nome == tipo
    porcentagem = (len(dados[ocorrencia]) * 100) / len(dados)
    print("----------------------------------------Dados Abaixo----------------------------------------")
    print(f"\nOcorrências do tipo {tipo}\n")
    print(dados[ocorrencia])
    print(len(ocorrencia))
    print(f"\nDas {len(dados)} ocorrências, {len(dados[ocorrencia])} são de {tipo}")
    print(f"O que equivale à {round(porcentagem,2)}%")
