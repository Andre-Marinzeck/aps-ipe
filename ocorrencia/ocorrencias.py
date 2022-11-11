import pandas as pd

url = "https://dedalo.sti.fab.mil.br/dadosabertos/ocorrencia.csv"
dados = pd.read_csv(url, sep=';', encoding='latin-1')


# Ocorrencias por classificação

def classificacao():
    i = 0
    while (i == 0):
        print("1 - Acidente")
        print("2 - Incidente")
        print("3 - Incidente Grave")
        print("4 - Sair")
        opcao = int(input("\n Digite uma das opções: "))
        if (opcao > 4) | (opcao < 1):
            print("\n  OPÇÃO INVALIDA - TENTE NOVAMENTE \n")
        else:
            if (opcao == 1):
                classificacao = dados.ocorrencia_classificacao == 'ACIDENTE'
            if (opcao == 2):
                classificacao = dados.ocorrencia_classificacao == 'INCIDENTE'
            if (opcao == 3):
                classificacao = dados.ocorrencia_classificacao == 'INCIDENTE GRAVE'
        ocorrencia = dados[classificacao].loc[:, ['codigo_ocorrencia', 'ocorrencia_classificacao',
                                                  'ocorrencia_cidade', 'ocorrencia_uf']]
        if (opcao == 4):
            i == 1
        print(ocorrencia)


# Ocorrencias por status

def status():
    i = 0
    while (i == 0):
        print("1 - Ativo")
        print("2 - Finalizada")
        print("3 - Sair de Status")
        opcao = int(input("\n Digite uma das opções: "))
        if (opcao > 3) | (opcao < 1):
            print("\n  OPÇÃO INVALIDA - TENTE NOVAMENTE \n")
        else:
            if (opcao == 1):
                classificacao = dados.investigacao_status == "ATIVA"
            if (opcao == 2):
                classificacao = dados.investigacao_status == "FINALIZADA"
        ocorrencia = dados[classificacao].loc[:, ['codigo_ocorrencia', 'ocorrencia_classificacao',
                                                  'ocorrencia_cidade', 'ocorrencia_uf', 'investigacao_status']]
        if (opcao == 3):
            i = 1
        print(ocorrencia)


# Pesquisa por cidades

def pesquisaCidade():
    cidade = input("Digite a cidade que gostaria de ver: ").upper()
    classificacao = dados.ocorrencia_cidade == cidade
    ocorrencia = dados[classificacao].loc[:, ['codigo_ocorrencia', 'ocorrencia_classificacao',
                                              'ocorrencia_cidade', 'ocorrencia_uf']]
    print(ocorrencia)
