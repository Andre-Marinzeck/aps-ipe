from .ocorrencias import *

def ocorrencia():
    i = 0
    while (i == 0):
        print("--------------------------------------------------------------------------------------------")
        print("\n Qual tipo de ocorrência gostaria de ver? \n")
        print("1 - Classificação")
        print("2 - Status das Ocorrência")
        print("3 - Pesquisa por Cidade")
        print("4 - Sair de Ocorrências")
        opcao = int(input("\n Digite uma das opções: "))
        if (opcao > 4) | (opcao < 1):
            print("\n  OPÇÃO INVALIDA - TENTE NOVAMENTE \n")
        else:
            if (opcao == 1):
                classificacao()
            if (opcao == 2):
                status()
            if (opcao == 3):
                pesquisaCidade()
            if (opcao == 4):
                i = 1
