import pandas as pd
import numpy as np
from helpers import calendario, formulas
from padroes import DECIMAIS_VALOR_FINANCEIRO_CUPOM
from datetime import datetime, timedelta


class TesouroPrefixadoComJurosSemetrais:
    """Os títulos do tesouro prefixado com juros semestrais possuem fluxo de pagamento de juros semestrais."""
    def __init__(self, data_compra, data_vencimento, valor_investido, rentabilidade_anual):

        self.data_compra = data_compra
        self.data_vencimento = data_vencimento
        self.valor_investido = valor_investido
        self.rentabilidade_anual = rentabilidade_anual
        self.datas_pagamento_cupom = self.descobrir_datas_pagamento_cupom()
        self.preco_unitario = self.calcular_preco_unitario()

    def calcular_preco_unitario(self):
        data_compra = calendario.coverte_formato_data(self.data_compra)
        data_vencimento = calendario.coverte_formato_data(self.data_vencimento)
        dias_uteis = calendario.calcula_dias_uteis(data_inicio=data_compra, data_fim=data_vencimento)

        preco_unitario = 1000 / ((1 + self.rentabilidade_anual) ** (dias_uteis / 252))
        preco_unitario = formulas.truncar(numero=preco_unitario, casas=2)

        return preco_unitario


    def descobrir_datas_pagamento_cupom(self):
        data_compra_timestamp = datetime.strptime(self.data_compra, "%d/%m/%Y")
        data_vencimento_timestamp = datetime.strptime(self.data_vencimento, "%d/%m/%Y")

        # TODO - Precisa melhorar esse loop
        datas_pagamento_cupom = []
        while data_compra_timestamp <= data_vencimento_timestamp:
            if (data_compra_timestamp.month == 7 or data_compra_timestamp.month == 1) and data_compra_timestamp.day == 1:
                data_cupom = data_compra_timestamp.strftime("%Y-%m-%d")
                datas_pagamento_cupom.append(data_cupom)
            data_compra_timestamp = data_compra_timestamp + timedelta(days=1)
        return datas_pagamento_cupom

    def calcular_valor_nominal(self):
        taxa_cupom = formulas.converte_taxa_ano_para_semestre(taxa=0.10)
        taxa_cupom = formulas.truncar(numero=taxa_cupom, casas=4)


        valor_cupom = ((self.valor_investido / self.preco_unitario) * taxa_cupom) * 1000
        valor_cupom = formulas.truncar(numero=valor_cupom, casas=2)

        data_compra = calendario.coverte_formato_data(self.data_compra)
        dias_corridos = []
        for dia_de_pagamento in self.datas_pagamento_cupom:
            dias_corridos.append(calendario.calcula_dias_uteis(data_inicio=data_compra, data_fim=dia_de_pagamento))


        print('a')



if __name__ == '__main__':
    titulo_1 = TesouroPrefixadoComJurosSemetrais(
        data_compra='20/03/2021',
        data_vencimento='01/01/2031',
        valor_investido=2000,
        rentabilidade_anual=0.0859
    )
    titulo_1_valor_nominal = titulo_1.calcular_valor_nominal()
    print(titulo_1_valor_nominal)
