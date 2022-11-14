import pandas as pd

url = "https://dedalo.sti.fab.mil.br/dadosabertos/ocorrencia.csv"
dados = pd.read_csv(url, sep=';', encoding='latin-1')


# Ocorrencias por classificação

def classificacao():
    while (True):
        print("1 - Acidente")
        print("2 - Incidente")
        print("3 - Incidente Grave")
        print("4 - Sair")
        opcao = int(input("\n Digite uma das opções: "))
        if (opcao > 4) | (opcao < 1):
            print("\n  OPÇÃO INVALIDA - TENTE NOVAMENTE \n")
        else:
            if (opcao == 1):
                status = "Acidentes"
                classificacao = dados.ocorrencia_classificacao == 'ACIDENTE'
            if (opcao == 2):
                status = "Incidentes"
                classificacao = dados.ocorrencia_classificacao == 'INCIDENTE'
            if (opcao == 3):
                status = "Incidentes Grave"
                classificacao = dados.ocorrencia_classificacao == 'INCIDENTE GRAVE'
            if (opcao == 4):
                break
            ocorrencia = dados[classificacao].loc[:, ['codigo_ocorrencia', 'ocorrencia_classificacao',
                                                    'ocorrencia_cidade', 'ocorrencia_uf']]
            porcentagem = (len(ocorrencia) * 100) / len(dados)
            print(ocorrencia)
            print(f"\nDas {len(dados)} ocorrencias, {len(ocorrencia)} são {status} ")
            print(f"O que equivale à {round(porcentagem,2)}%")
            print("---------------------------------------------------------------------------------------")



# Ocorrencias por status

def status():
    while (True):
        print("1 - Ativa")
        print("2 - Finalizada")
        print("3 - Sair de Status")
        opcao = int(input("\n Digite uma das opções: "))
        if (opcao > 3) | (opcao < 1):
            print("\n  OPÇÃO INVALIDA - TENTE NOVAMENTE \n")
        else:
            if (opcao == 1):
                status = "Ativa"
                classificacao = dados.investigacao_status == "ATIVA"
            if (opcao == 2):
                status = "Finalizada"
                classificacao = dados.investigacao_status == "FINALIZADA"
            if (opcao == 3):
                break
        ocorrencia = dados[classificacao].loc[:, ['codigo_ocorrencia', 'ocorrencia_classificacao',
                                                  'ocorrencia_cidade', 'ocorrencia_uf', 'investigacao_status']]
        porcentagem = (len(ocorrencia) * 100) / len(dados)
        print(ocorrencia)
        print(f"\nDas {len(dados)} ocorrencias, {len(ocorrencia)} estão {status} ")
        print(f"O que equivale à {round(porcentagem,2)}%")
        print("---------------------------------------------------------------------------------------")



# Pesquisa por cidades

def pesquisaCidade():
    cidade = input("Digite a cidade que gostaria de ver: ").upper()
    classificacao = dados.ocorrencia_cidade == cidade
    ocorrencia = dados[classificacao].loc[:, ['codigo_ocorrencia', 'ocorrencia_classificacao',
                                              'ocorrencia_cidade', 'ocorrencia_uf']]
    porcentagem = (len(ocorrencia) * 100) / len(dados)
    print(ocorrencia)
    print(f"\nDas {len(dados)} ocorrencias, {len(ocorrencia)} são em {cidade}")
    print(f"O que equivale à {round(porcentagem,2)}%")
    print("---------------------------------------------------------------------------------------")

