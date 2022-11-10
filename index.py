import pandas as pd

url = "https://dedalo.sti.fab.mil.br/dadosabertos/ocorrencia.csv";
dados = pd.read_csv(url, sep=';', encoding='latin-1');
print(dados)