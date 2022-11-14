from analise.analiseView import analises
from ocorrencia.ocorrenciaView import ocorrencia
from ocorrenciaTipo.ocorrenciasTipoView import TipoOcorrencia
from aeronave.aeronaveView import aeronaves
from fatorContribuinte.fatorView import fatorContribuinte
from recomendacoes.recomendacoesView import recomendacoes

i = 0
while (i == 0):
    print("--------------------------------------------------------------------------------------------")
    print("\n Escolha uma das opções abaixo \n")
    print("1 - Ocorrência")
    print("2 - Tipo de Ocorrência")
    print("3 - Tabela de Aeronave")
    print("4 - Fator Contribuinte")
    print("5 - Recomendações")
    print("6 - Análises Críticas")
    print("7 - Sair")
    opcao = int(input("\n Digite uma da opções: "))
    if (opcao > 7) | (opcao < 1):
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
            analises()
        if (opcao == 7):
            i = 1