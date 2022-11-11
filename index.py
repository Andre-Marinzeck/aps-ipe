from ocorrencia.ocorrenciaView import *

i = 0

while (i == 0):
    print("\n Escolha uma das opções abaixo \n")
    print("1 - Ocorrencia")
    print("2 - Tipo de Ocorrencia")
    print("3 - Tabela de Aeronave")
    print("4 - Fator Contribuinte")
    print("5 - Recomendações")
    print("6 - Sair")
    opcao = int(input("\n Digite uma da opções: "))
    if (opcao > 6) | (opcao < 1):
        print("\n  OPÇÃO INVALIDA - TENTE NOVAMENTE \n")
    else:
        if (opcao == 1):
            ocorrencia()
        if (opcao == 2):
            ocorrencia()
        if (opcao == 3):
            ocorrencia()
        if (opcao == 4):
            ocorrencia()
        if (opcao == 5):
            ocorrencia()
        if (opcao == 6):
            i = 1
