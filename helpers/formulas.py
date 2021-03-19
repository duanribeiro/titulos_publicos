import math
from padroes import DECIMAIS_TAXAS_EQUIVALENTES, DECIMAIS_TX_CUPOM


def truncar(numero, casas):
    if type(numero) == int:
        return numero

    splitted_number = str(numero).split('.')
    return float(f'{splitted_number[0]}.{splitted_number[1][:casas]}')


def arredondar_para_cima(numero, decimais=2):
    if not isinstance(decimais, int):
        raise TypeError("decimal places must be an integer")
    elif decimais < 0:
        raise ValueError("decimal places has to be 0 or more")
    elif decimais == 0:
        return math.ceil(numero)

    factor = 10 ** decimais
    return math.ceil(numero * factor) / factor


def calcula_montante_juros_compostos(valor_investido, taxa, periodo):
    montante = valor_investido * ((1 + taxa) ** periodo)
    return round(montante, DECIMAIS_TX_CUPOM)


def converte_tx_ano_para_dia(taxa):
    taxa_convertida = ((1 + taxa) ** (1 / 252)) - 1
    return truncar(numero=taxa_convertida, casas=DECIMAIS_TAXAS_EQUIVALENTES)


def converte_tx_ano_para_semestre(taxa):
    return ((1 + taxa) ** (1 / 2)) - 1



