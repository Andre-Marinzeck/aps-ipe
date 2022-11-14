from .recomendacoes import *

def recomendacoes():
    i = 0
    while (i == 0):
        print("--------------------------------------------------------------------------------------------")
        print("\n Qual tipo de recomendações gostaria de ver? \n")
        print("1 - IMPLEMENTADA")
        print("2 - NÃO IMPLEMENTADA")
        print("3 - IMPLEMENTADA DE FORMA ALTERNATIVA")
        print("4 - AGUARDANDO RESPOSTA")
        print("5 - Sair de Recomendações")
        opcao = int(input("\n Digite uma das opções: "))
        if (opcao > 5) | (opcao < 1):
            print("\n  OPÇÃO INVALIDA - TENTE NOVAMENTE \n")
        else:
            if (opcao == 1):
                recomendacao("IMPLEMENTADA")
            if (opcao == 2):
                recomendacao("NÃO IMPLEMENTADA")
            if (opcao == 3):
                recomendacao("IMPLEMENTADA DE FORMA ALTERNATIVA")
            if (opcao == 4):
                recomendacao("AGUARDANDO RESPOSTA")
            if (opcao == 5):
                i = 1