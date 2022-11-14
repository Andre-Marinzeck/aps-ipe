import pandas as pd

ocorrencia ="https://dedalo.sti.fab.mil.br/dadosabertos/ocorrencia.csv"
ocorrenciaDados = pd.read_csv(ocorrencia, sep=";", encoding="latin-1")

fator = "https://dedalo.sti.fab.mil.br/dadosabertos/fator_contribuinte.csv"
fatorDados = pd.read_csv(fator, sep=";", encoding="UTF-8")

aero = "https://dedalo.sti.fab.mil.br/dadosabertos/aeronave.csv"
aeroDados = pd.read_csv(aero, sep=";", encoding="UTF-8")

def topCidades():
    topCidade = ocorrenciaDados["ocorrencia_cidade"].value_counts()
    print("----------------------------------------Dados Abaixo----------------------------------------")
    print("\nCidades com o maior número de ocorrências\n")
    print(topCidade.head(10))

def topFator():
    topFator = fatorDados["fator_nome"].value_counts()
    print("----------------------------------------Dados Abaixo----------------------------------------")
    print("\nFator de acidentes mais comuns\n")
    print(topFator.head(10))

def topDanos():
    topDano = aeroDados["aeronave_nivel_dano"].value_counts()
    print("----------------------------------------Dados Abaixo----------------------------------------")
    print("\nNíveis de dano em aeronaves\n")
    print(topDano)

def horario():
    topHorario = ocorrenciaDados["ocorrencia_hora"].value_counts()
    print("----------------------------------------Dados Abaixo----------------------------------------")
    print("\nHorários com mais ocorrências\n")
    print(topHorario.head(10))

def mediaRibeirao():
    cidade = ocorrenciaDados.ocorrencia_cidade == "RIBEIRÃO PRETO"
    acidente = ocorrenciaDados.ocorrencia_classificacao == "ACIDENTE"
    incidente = ocorrenciaDados.ocorrencia_classificacao == "INCIDENTE"
    incidenteGrave = ocorrenciaDados.ocorrencia_classificacao == "INCIDENTE GRAVE"
    porcentagemTotal = (len(ocorrenciaDados[cidade]) * 100) / len(ocorrenciaDados)
    porcentagemA = (len(ocorrenciaDados[(cidade) & (acidente)]) * 100) / len(ocorrenciaDados)
    porcentagemI = (len(ocorrenciaDados[(cidade) & (incidente)]) * 100) / len(ocorrenciaDados)
    porcentagemIG = (len(ocorrenciaDados[(cidade) & (incidenteGrave)]) * 100) / len(ocorrenciaDados)
    print("----------------------------------------Dados Abaixo----------------------------------------")
    print("\nMédia de ocorrências em Ribeirão Preto\n")
    print(f"Das {len(ocorrenciaDados)} ocorrencias, {len(ocorrenciaDados[cidade])} ({round(porcentagemTotal, 2)}%) são em Ribeirão Preto")
    print(f"Onde {len(ocorrenciaDados[(cidade) & (acidente)])} ({round(porcentagemA, 2)}%) São de Acidentes")
    print(f"Onde {len(ocorrenciaDados[(cidade) & (incidente)])} ({round(porcentagemI, 2)}%) São de Incidentes")
    print(f"Onde {len(ocorrenciaDados[(cidade) & (incidenteGrave)])} ({round(porcentagemIG, 2)}%) São de Incidentes Graves")
