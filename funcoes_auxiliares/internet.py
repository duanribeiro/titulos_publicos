from funcoes_auxiliares import formulas
import requests
from bs4 import BeautifulSoup


def requisicao_valor_nominal_atualizado():
    dados = {
        'Data': '29032021',
        'escolha': '1',
        'Idioma': 'PT',
        'saida': 'xls',
        'Dt_Ref_Ver': '20210322',
        'Inicio': '29 / 03 / 2021'
    }

    resposta_http = requests.post('https://www.anbima.com.br/informacoes/vna/vna.asp', data=dados)
    resposta_html = BeautifulSoup(resposta_http.text, 'html.parser')
    vna_ipca_com_juros = resposta_html.select('tr')[8].select('td')[1].text
    vna_selic = resposta_html.select('tr')[19].select('td')[1].text

    vna_ipca_com_juros = float(vna_ipca_com_juros.replace('.', '').replace(',', '.'))
    vna_selic = float(vna_selic.replace('.', '').replace(',', '.'))
    vna_ipca_com_juros = formulas.truncar(numero=vna_ipca_com_juros, decimais=2)
    vna_selic = formulas.truncar(numero=vna_selic, decimais=2)

    return {
        'vna_ipca_com_juros': vna_ipca_com_juros,
        'vna_selic': vna_selic
    }


