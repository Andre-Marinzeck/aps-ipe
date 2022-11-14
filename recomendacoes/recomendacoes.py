import pandas as pd

url = "https://dedalo.sti.fab.mil.br/dadosabertos/recomendacao.csv"
dados = pd.read_csv(url, sep=';', encoding='utf-8')


def recomendacao(tipo):
    ocorrencia = dados.recomendacao_status == tipo
    view = dados[ocorrencia].loc[:, ["recomendacao_conteudo", "recomendacao_status", "recomendacao_destinatario"]]
    porcentagem = (len(view) * 100) / len(dados)
    print("----------------------------------------Dados Abaixo----------------------------------------")
    print(f"\nRecomendações: {tipo}\n")
    print(view)
    print(len(ocorrencia))
    print(
        f"\nDas {len(dados)} recomendações, {len(view)} está {tipo}")
    print(f"O que equivale à {round(porcentagem,2)}%")
