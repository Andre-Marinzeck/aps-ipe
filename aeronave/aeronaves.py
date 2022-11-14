import pandas as pd

url = "https://dedalo.sti.fab.mil.br/dadosabertos/aeronave.csv"
dados = pd.read_csv(url, sep=';', encoding='UTF-8')

def aeronaveTipo():
    while (True):
        print("--------------------------------------------------------------------------------------------")
        print("\n Qual tipo de aeronave gostaria de ver? \n")
        print("1 - Avião")
        print("2 - Helicóptero")
        print("3 - Ultraleve")
        print("4 - Sair de Tipo de Aeronaves")
        opcao = int(input("\n Digite uma das opções: "))
        if (opcao > 4) | (opcao < 1):
            print("\n  OPÇÃO INVALIDA - TENTE NOVAMENTE \n")
        else:
            if (opcao == 1):
                status = "AVIÃOES"
                tipo = dados.aeronave_tipo_veiculo == 'AVIÃO'
            if (opcao == 2):
                status = "HELICÓPTEROS"
                tipo = dados.aeronave_tipo_veiculo == 'HELICÓPTERO'
            if (opcao == 3):
                status = "ULTRALEVES"
                tipo = dados.aeronave_tipo_veiculo == 'ULTRALEVE'
            if (opcao == 4):
                break
        ocorrencia = dados[tipo].loc[:, ['aeronave_matricula', 'aeronave_tipo_veiculo',
                                                    'aeronave_fabricante', 'aeronave_nivel_dano']]
        porcentagem = (len(ocorrencia) * 100) / len(dados)
        print("----------------------------------------Dados Abaixo----------------------------------------")
        print(ocorrencia)
        print(f"\nDas {len(dados)} aeronaves, {len(ocorrencia)} é de {status}")
        print(f"O que equivale à {round(porcentagem,2)}%")
        


def motorTipo():
    while (True):
        print("--------------------------------------------------------------------------------------------")
        print("\n Qual tipo de motor gostaria de ver? \n")
        print("1 - PISTÃO")
        print("2 - JATO")
        print("3 - TURBOÉLICE")
        print("4 - TURBOEIXO")
        print("5 - Sair de Tipo de Motor")
        opcao = int(input("\n Digite uma das opções: "))
        if (opcao > 5) | (opcao < 1):
            print("\n  OPÇÃO INVALIDA - TENTE NOVAMENTE \n")
        else:
            if (opcao == 1):
                status = "PISTÃO"
                tipo = dados.aeronave_motor_tipo == 'PISTÃO'
            if (opcao == 2):
                status = "JATO"
                tipo = dados.aeronave_motor_tipo == 'JATO'
            if (opcao == 3):
                status = "TURBOÉLICE"
                tipo = dados.aeronave_motor_tipo == 'TURBOÉLICE'
            if (opcao == 4):
                status = "TURBOEIXO"
                tipo = dados.aeronave_motor_tipo == 'TURBOEIXO'
            if (opcao == 5):
                break
        ocorrencia = dados[tipo].loc[:, ['aeronave_matricula', 'aeronave_motor_tipo',
                                                    'aeronave_fabricante', 'aeronave_nivel_dano']]
        porcentagem = (len(ocorrencia) * 100) / len(dados)
        print("----------------------------------------Dados Abaixo----------------------------------------")
        print(ocorrencia)
        print(f"\nDas {len(dados)} aeronaves, {len(ocorrencia)} é do tipo {status}")
        print(f"O que equivale à {round(porcentagem,2)}%")


def segmento():
    while (True):
        print("--------------------------------------------------------------------------------------------")
        print("\n Qual tipo de segmento gostaria de ver? \n")
        print("1 - TÁXI AÉREO")
        print("2 - INSTRUÇÃO")
        print("3 - ESPECIALIZADA")
        print("4 - REGULAR")
        print("5 - NÃO REGULAR")
        print("6 - PARTICULAR")
        print("7 - AGRÍCOLA")
        print("8 - EXPERIMENTAL")
        print("9 - Sair de segmento")
        opcao = int(input("\n Digite uma das opções: "))
        if (opcao > 9) | (opcao < 1):
            print("\n  OPÇÃO INVALIDA - TENTE NOVAMENTE \n")
        else:
            if (opcao == 1):
                status = "TÁXI AÉREO"
                tipo = dados.aeronave_registro_segmento == 'TÁXI AÉREO'
            if (opcao == 2):
                status = "INSTRUÇÃO"
                tipo = dados.aeronave_registro_segmento == 'INSTRUÇÃO'
            if (opcao == 3):
                status = "ESPECIALIZADA"
                tipo = dados.aeronave_registro_segmento == 'ESPECIALIZADA'
            if (opcao == 4):
                status = "REGULAR"
                tipo = dados.aeronave_registro_segmento == 'REGULAR'
            if (opcao == 5):
                status = "NÃO REGULAR"
                tipo = dados.aeronave_registro_segmento == 'NÃO REGULAR'
            if (opcao == 6):
                status = "PARTICULAR"
                tipo = dados.aeronave_registro_segmento == 'PARTICULAR'
            if (opcao == 7):
                status = "AGRÍCOLA"
                tipo = dados.aeronave_registro_segmento == 'AGRÍCOLA'
            if (opcao == 8):
                status = "EXPERIMENTAL"
                tipo = dados.aeronave_registro_segmento == 'EXPERIMENTAL'
            if (opcao == 9):
                break
        ocorrencia = dados[tipo].loc[:, ['aeronave_matricula', 'aeronave_registro_segmento',
                                                    'aeronave_fabricante', 'aeronave_nivel_dano']]
        porcentagem = (len(ocorrencia) * 100) / len(dados)
        print("----------------------------------------Dados Abaixo----------------------------------------")
        print(ocorrencia)
        print(f"\nDas {len(dados)} aeronaves, {len(ocorrencia)} é do tipo {status}")
        print(f"O que equivale à {round(porcentagem,2)}%")
