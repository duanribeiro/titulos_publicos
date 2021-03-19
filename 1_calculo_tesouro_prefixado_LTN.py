from helpers import calendario, formulas
from padroes import DECIMAIS_DINHEIRO_ESPECIE


def calculo_montante_LTN(data_compra, data_vencimento, valor_investido, rentabilidade_anual):
    data_compra = calendario.coverte_formato_data(data_compra)
    data_vencimento = calendario.coverte_formato_data(data_vencimento)
    data_vencimento = calendario.remover_dias_uteis(data=data_vencimento, dias=1)
    dias_uteis = calendario.calcula_dias_uteis(data_inicio=data_compra, data_fim=data_vencimento)

    preco_unitario = 1000 / ((1 + rentabilidade_anual) ** (dias_uteis / 252))
    preco_unitario = formulas.truncar(numero=preco_unitario, casas=DECIMAIS_DINHEIRO_ESPECIE)

    montante = (valor_investido / preco_unitario) * 1000

    return montante


if __name__ == '__main__':
    resultado = calculo_montante_LTN(
        data_compra='19/03/2021',
        data_vencimento='01/09/2024',
        valor_investido=788.66,
        rentabilidade_anual=0.0754
    )

    print(resultado)
