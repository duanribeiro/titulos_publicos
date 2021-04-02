from funcoes_auxiliares import calendario, formulas
from datetime import datetime


class TesouroPrefixadoComJurosSemetrais:
    """Os títulos do tesouro prefixado com juros semestrais possuem fluxo de pagamento de juros semestrais."""
    def __init__(self, data_compra, data_vencimento, valor_investido, rentabilidade_anual, preco_unitario=None):

        self.data_compra = data_compra
        self.data_vencimento = data_vencimento
        self.valor_investido = valor_investido
        self.rentabilidade_anual = rentabilidade_anual
        self.datas_pagamento_cupom, self.dias_uteis = self.descobrir_datas_pagamento_cupom()
        self.preco_unitario = preco_unitario if preco_unitario else self.calcular_preco_unitario()

    def calcular_preco_unitario(self):
        preco_unitario = 0
        for dia in self.dias_uteis[:-1]:
            preco_unitario += 48.81 / ((1 + self.rentabilidade_anual) ** (dia / 252))
        preco_unitario += (1000 + 48.81) / ((1 + self.rentabilidade_anual) ** (dia / 252))
        preco_unitario = formulas.truncar(numero=preco_unitario, decimais=2)

        return preco_unitario

    def descobrir_datas_pagamento_cupom(self):
        data_compra_timestamp = datetime.strptime(self.data_compra, "%d/%m/%Y")
        data_vencimento_timestamp = datetime.strptime(self.data_vencimento, "%d/%m/%Y")

        datas_pagamento_cupom = []
        if 1 < data_compra_timestamp.month < 7:
            for ano in range(data_compra_timestamp.year, data_vencimento_timestamp.year):
                datas_pagamento_cupom.append(f"{ano}-07-01")
                datas_pagamento_cupom.append(f"{ano + 1}-01-01")
        else:
            for ano in range(data_compra_timestamp.year, data_vencimento_timestamp.year):
                datas_pagamento_cupom.append(f"{ano + 1}-01-01")
                datas_pagamento_cupom.append(f"{ano + 1}-07-01")

        if data_vencimento_timestamp.month > 1:
            datas_pagamento_cupom.pop(-1)

        dias_uteis = []
        data_compra = calendario.coverte_formato_data(self.data_compra)
        for dia_de_pagamento in datas_pagamento_cupom:
            dias_uteis.append(calendario.calcula_dias_uteis(data_inicio=data_compra, data_fim=dia_de_pagamento))

        return datas_pagamento_cupom, dias_uteis

    def calcular_valor_nominal(self):
        # taxa_cupom = formulas.converte_taxa_ano_para_semestre(taxa=0.10)
        # taxa_cupom = formulas.truncar(numero=taxa_cupom, decimais=4)
        taxa_cupom = 0.04881
        valor_cupom = ((self.valor_investido / self.preco_unitario) * taxa_cupom) * 1000
        valor_cupom = formulas.truncar(numero=valor_cupom, decimais=2)

        valor_bruto_cupons = valor_cupom * len(self.datas_pagamento_cupom)
        valor_nominal = ((self.valor_investido / self.preco_unitario) * 1000) + valor_bruto_cupons
        valor_nominal = formulas.arredondar_para_cima(numero=valor_nominal, decimais=2)
        return valor_nominal


if __name__ == '__main__':
    titulo_1 = TesouroPrefixadoComJurosSemetrais(
        data_compra='27/03/2021',
        data_vencimento='01/01/2031',
        valor_investido=5000,
        rentabilidade_anual=0.0918,
        preco_unitario=1074.95,
    )
    titulo_1_valor_nominal = titulo_1.calcular_valor_nominal()
    print(titulo_1_valor_nominal)
