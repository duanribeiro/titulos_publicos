from helpers import calendario, formulas
from padroes import DECIMAIS_DINHEIRO_ESPECIE


class TesouroPrefixado:
    def __init__(self, data_compra, data_vencimento, valor_investido, rentabilidade_anual, preco_unitario=None):
        self.data_compra = data_compra
        self.data_vencimento = data_vencimento
        self.valor_investido = valor_investido
        self.rentabilidade_anual = rentabilidade_anual
        self.preco_unitario = preco_unitario if preco_unitario else self.calcular_preco_unitario()

    def calcular_preco_unitario(self):
        data_compra = calendario.coverte_formato_data(self.data_compra)
        data_vencimento = calendario.coverte_formato_data(self.data_vencimento)
        dias_uteis = calendario.calcula_dias_uteis(data_inicio=data_compra, data_fim=data_vencimento)
        preco_unitario = 1000 / ((1 + self.rentabilidade_anual) ** (dias_uteis / 252))
        preco_unitario = formulas.truncar(numero=preco_unitario, decimais=DECIMAIS_DINHEIRO_ESPECIE)

        return preco_unitario

    def calcular_valor_nominal(self):
        valor_nominal = (self.valor_investido / self.preco_unitario) * 1000
        valor_nominal = formulas.arredondar_para_cima(numero=valor_nominal, decimais=DECIMAIS_DINHEIRO_ESPECIE)

        return valor_nominal


if __name__ == '__main__':
    titulo_1 = TesouroPrefixado(
        data_compra='19/03/2021',
        data_vencimento='01/09/2024',
        valor_investido=788.66,
        rentabilidade_anual=0.0754
    )
    titulo_1_valor_nominal = titulo_1.calcular_valor_nominal()
    print(titulo_1_valor_nominal)
