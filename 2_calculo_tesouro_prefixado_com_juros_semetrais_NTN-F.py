import pandas as pd
from helpers import calendario, formulas
from padroes import DECIMAIS_TX_CUPOM


def calculo_montante_NTNF(data_compra, data_vencimento, valor_investido, preco_unitario):
    datas_pagamento_cupom = ['01-01', '07-01']
    taxa_de_negociacao = 0.0001
    taxa_cupom = formulas.converte_tx_ano_para_semestre(taxa=0.10)
    valor_investido_bruto = valor_investido * (1 + taxa_de_negociacao)
    cupom_bruto = ((valor_investido_bruto / preco_unitario) * taxa_cupom) * 1000
    cupom_bruto = formulas.arredondar_para_cima(numero=cupom_bruto, decimais=DECIMAIS_TX_CUPOM)

    data_compra = calendario.coverte_formato_data(data_compra)
    data_vencimento = calendario.coverte_formato_data(data_vencimento)
    dias_corridos = pd.date_range(start=data_compra, end=data_vencimento)

    fluxo_de_caixa = 0
    for dia in dias_corridos:
        if dia.strftime('%m-%d') in datas_pagamento_cupom:
            fluxo_de_caixa += cupom_bruto

            formulas.converte_tx_ano_para_dia(10)
    montante = fluxo_de_caixa + ((valor_investido / preco_unitario) * 1000)

    return montante


if __name__ == '__main__':
    resultado = calculo_montante_NTNF(
        data_compra='02/03/2021',
        data_vencimento='01/01/2031',
        valor_investido=2000,
        preco_unitario=1101.43,
        rentabilidade_anual=0.0867
    )
