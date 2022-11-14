from .ocorrenciasTipo import *

def TipoOcorrencia():
    i = 0
    while (i == 0):
        print("--------------------------------------------------------------------------------------------")
        print("\n Qual tipo de ocorrência gostaria de ver? \n")
        print("1 - ESTOURO DE PNEU")
        print("2 - EXCURSÃO DE PISTA")
        print("3 - DESCOMPRESSÃO NÃO INTENCIONAL / EXPLOSIVA")
        print("4 - FALHA OU MAU FUNCIONAMENTO DE SISTEMA / COMPONENTE")
        print("5 - COLISÃO COM OBSTÁCULO DURANTE A DECOLAGEM E POUSO")
        print("6 - PERDA DE CONTROLE EM VOO")
        print("7 - PERDA DE CONTROLE NO SOLO")
        print("8 - FALHA DO MOTOR EM VOO")
        print("9 - INDETERMINADO")
        print("10 - VAZAMENTO DE COMBUSTÍVEL")
        print("11 - CONTATO ANORMAL COM A PISTA")
        print("12 - TRÁFEGO AÉREO")
        print("13 - COLISÃO COM AVE")
        print("14 - Sair de Ocorrências")
        opcao = int(input("\n Digite uma das opções: "))
        if (opcao > 14) | (opcao < 1):
            print("\n  OPÇÃO INVALIDA - TENTE NOVAMENTE \n")
        else:
            if (opcao == 1):
                tipo("ESTOURO DE PNEU")
            if (opcao == 2):
                tipo("EXCURSÃO DE PISTA")
            if (opcao == 3):
                tipo("DESCOMPRESSÃO NÃO INTENCIONAL / EXPLOSIVA")
            if (opcao == 4):
                tipo("FALHA OU MAU FUNCIONAMENTO DE SISTEMA / COMPONENTE")
            if (opcao == 5):
                tipo("COLISÃO COM OBSTÁCULO DURANTE A DECOLAGEM E POUSO")
            if (opcao == 6):
                tipo("PERDA DE CONTROLE EM VOO")
            if (opcao == 7):
                tipo("PERDA DE CONTROLE NO SOLO")
            if (opcao == 8):
                tipo("FALHA DO MOTOR EM VOO")
            if (opcao == 9):
                tipo("INDETERMINADO")
            if (opcao == 10):
                tipo("VAZAMENTO DE COMBUSTÍVEL")
            if (opcao == 11):
                tipo("CONTATO ANORMAL COM A PISTA")
            if (opcao == 12):
                tipo("TRÁFEGO AÉREO")
            if (opcao == 13):
                tipo("COLISÃO COM AVE")
            if (opcao == 14):
                i = 1
