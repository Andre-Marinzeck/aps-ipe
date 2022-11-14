from .fator import *

def fatorContribuinte():
    i = 0
    while (i == 0):
        print("---------------------------------------------------------------------------------------")
        print("\n Qual tipo de ocorrencia gostaria de ver? \n")
        print("1 - ATITUDE")
        print("2 - JULGAMENTO DE PILOTAGEM")
        print("3 - PLANEJAMENTO DE VOO")
        print("4 - SUPERVISÃO GERENCIAL")
        print("5 - POUCA EXPERIÊNCIA DO PILOTO")
        print("6 - PROCESSO DECISÓRIO")
        print("7 - INFRAESTRUTURA AEROPORTUÁRIA")
        print("8 - PRESENÇA DE FAUNA (NÃO AVE)")
        print("9 - MANUTENÇÃO DA AERONAVE")
        print("10 - PERCEPÇÃO")
        print("11 - APLICAÇÃO DE COMANDOS")
        print("12 - CONDIÇÕES METEOROLÓGICAS ADVERSAS")
        print("13 - ATENÇÃO")
        print("14 - CAPACITAÇÃO E TREINAMENTO")
        print("15 - INSTRUÇÃO")
        print("16 - OUTRO FATOR")
        print("17 - Sair de Fator Contribuinte")
        opcao = int(input("\n Digite uma das opções: "))
        if (opcao > 17) | (opcao < 1):
            print("\n  OPÇÃO INVALIDA - TENTE NOVAMENTE \n")
        else:
            if (opcao == 1):
                fator("ATITUDE")
            if (opcao == 2):
                fator("JULGAMENTO DE PILOTAGEM")
            if (opcao == 3):
                fator("PLANEJAMENTO DE VOO")
            if (opcao == 4):
                fator("SUPERVISÃO GERENCIAL")
            if (opcao == 5):
                fator("POUCA EXPERIÊNCIA DO PILOTO")
            if (opcao == 6):
                fator("PROCESSO DECISÓRIO")
            if (opcao == 7):
                fator("INFRAESTRUTURA AEROPORTUÁRIA")
            if (opcao == 8):
                fator("PRESENÇA DE FAUNA (NÃO AVE)")
            if (opcao == 9):
                fator("MANUTENÇÃO DA AERONAVE")
            if (opcao == 10):
                fator("PERCEPÇÃO")
            if (opcao == 11):
                fator("APLICAÇÃO DE COMANDOS")
            if (opcao == 12):
                fator("CONDIÇÕES METEOROLÓGICAS ADVERSAS")
            if (opcao == 13):
                fator("ATENÇÃO")
            if (opcao == 14):
                fator("CAPACITAÇÃO E TREINAMENTO")
            if (opcao == 15):
                fator("INSTRUÇÃO")
            if (opcao == 16):
                fator("OUTRO FATOR")
            if (opcao == 17):
                i = 1