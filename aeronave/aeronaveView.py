from .aeronaves import *

def aeronaves():
    i = 0
    while (i == 0):
        print("---------------------------------------------------------------------------------------")
        print("\n Qual tipo de ocorrencia gostaria de ver? \n")
        print("1 - Tipo de Aeronave")
        print("2 - Tipo de Motor")
        print("3 - Segmento")
        print("4 - Sair de Aeronaves")
        opcao = int(input("\n Digite uma das opções: "))
        if (opcao > 4) | (opcao < 1):
            print("\n  OPÇÃO INVALIDA - TENTE NOVAMENTE \n")
        else:
            if (opcao == 1):
                aeronaveTipo()
            if (opcao == 2):
                motorTipo()
            if (opcao == 3):
                segmento()
            if (opcao == 4):
                i = 1