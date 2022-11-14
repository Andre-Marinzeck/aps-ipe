from ocorrencia.ocorrenciaView import *
from ocorrenciaTipo.ocorrenciasTipoView import *
from aeronave.aeronaveView import *
from fatorContribuinte.fatorView import *
from recomendacoes.recomendacoesView import *

i = 0

while (i == 0):
    print("---------------------------------------------------------------------------------------")
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
            TipoOcorrencia()
        if (opcao == 3):
            aeronaves()
        if (opcao == 4):
            fatorContribuinte()
        if (opcao == 5):
            recomendacoes()
        if (opcao == 6):
            i = 1
