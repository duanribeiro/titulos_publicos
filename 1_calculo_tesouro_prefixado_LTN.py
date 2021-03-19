from helpers import calendario, formulas
from regras import DECIMAIS_DINHEIRO_VIVO, DECIMAIS_VALOR_FUTURO


def calculo_montante_LTN(data_compra, data_vencimento, valor_investido, rentabilidade_anual):
    data_compra = calendario.coverte_formato_data(data_compra)
    data_liquidacao_compra = calendario.adicionar_dias_uteis(data=data_compra, dias=1)
    data_vencimento = calendario.coverte_formato_data(data_vencimento)
    data_vencimento = calendario.remover_dias_uteis(data=data_vencimento, dias=1)
    dias_uteis = calendario.calcula_dias_uteis(data_inicio=data_liquidacao_compra, data_fim=data_vencimento)

    preco_unitario = 1000 / ((1 + rentabilidade_anual) ** (dias_uteis / 252))
    preco_unitario = formulas.truncar(numero=preco_unitario, casas=DECIMAIS_DINHEIRO_VIVO)

    montante = (valor_investido / preco_unitario) * 1000

    return montante


if __name__ == '__main__':
    resultado = calculo_montante_LTN(
        data_compra='06/03/2021',
        data_vencimento='01/07/2024',
        valor_investido=2000,
        rentabilidade_anual=0.0715
    )
