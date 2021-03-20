import pandas as pd
import numpy as np
from helpers import calendario, formulas
from padroes import DECIMAIS_VALOR_FINANCEIRO_CUPOM
from datetime import datetime, timedelta


def descobrir_datas_pagamento_cupom(data_compra, data_vencimento):
    timestamp_data_compra = datetime.strptime(data_compra, "%d/%m/%Y")
    timestamp_data_vencimento = datetime.strptime(data_vencimento, "%d/%m/%Y")

    datas_pagamento_cupom = []
    while timestamp_data_compra <= timestamp_data_vencimento:
        if (timestamp_data_compra.month == 7 or timestamp_data_compra.month == 1) and timestamp_data_compra.day == 1:
            data_cupom = timestamp_data_compra.strftime("%Y-%m-%d")
            while not np.is_busday(dates=data_cupom, weekmask='1111100', holidays=calendario.feriados):
                data_cupom = calendario.adicionar_dias_uteis(data=data_cupom, dias=1)
            datas_pagamento_cupom.append(data_cupom)
        timestamp_data_compra = timestamp_data_compra + timedelta(days=1)

    return datas_pagamento_cupom


def calculo_montante_NTNF(data_compra, data_vencimento, valor_investido, preco_unitario, rentabilidade_anual):
    datas_pagamento_cupom = descobrir_datas_pagamento_cupom(data_compra=data_compra, data_vencimento=data_vencimento)
    taxa_cupom = formulas.converte_tx_ano_para_semestre(taxa=0.10)
    taxa_cupom = formulas.truncar(numero=preco_unitario, casas=DECIMAIS_VALOR_FINANCEIRO_CUPOM)


    # taxa_de_negociacao = 0.0001
    # valor_investido_bruto = valor_investido * (1 + taxa_de_negociacao)
    # cupom_bruto = ((valor_investido_bruto / preco_unitario) * taxa_cupom) * 1000
    # cupom_bruto = formulas.arredondar_para_cima(numero=cupom_bruto, decimais=DECIMAIS_TX_CUPOM)
    #
    # data_compra = calendario.coverte_formato_data(data_compra)
    # data_vencimento = calendario.coverte_formato_data(data_vencimento)
    # dias_corridos = pd.date_range(start=data_compra, end=data_vencimento)
    #
    # fluxo_de_caixa = 0
    # for dia in dias_corridos:
    #     if dia.strftime('%m-%d') in datas_pagamento_cupom:
    #         fluxo_de_caixa += cupom_bruto
    #
    #         formulas.converte_tx_ano_para_dia(10)
    # montante = fluxo_de_caixa + ((valor_investido / preco_unitario) * 1000)
    #
    # return montante


if __name__ == '__main__':
    resultado = calculo_montante_NTNF(
        data_compra='29/10/2019',
        data_vencimento='01/01/2029',
        valor_investido=2000,
        preco_unitario=1101.43,
        rentabilidade_anual=0.0645
    )
