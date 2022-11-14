from .analise import *

def analises():
    i = 0
    while (i == 0):
        print("--------------------------------------------------------------------------------------------")
        print("\n Qual tipo de análise gostaria de ver? \n")
        print("1 - Cidades com o maior número de ocorrências")
        print("2 - Fator de acidentes mais comuns")
        print("3 - Níveis de dano em aeronaves")
        print("4 - Horários com mais ocorrências")
        print("5 - Média de ocorrências em Ribeirão Preto")
        print("6 - Sair de Análises Críticas")
        opcao = int(input("\n Digite uma das opções: "))
        if (opcao > 6) | (opcao < 1):
            print("\n  OPÇÃO INVALIDA - TENTE NOVAMENTE \n")
        else:
            if (opcao == 1):
                topCidades()
            if (opcao == 2):
                topFator()
            if (opcao == 3):
                topDanos()
            if (opcao == 4):
                horario()
            if (opcao == 5):
                mediaRibeirao()
            if (opcao == 6):
                i = 1