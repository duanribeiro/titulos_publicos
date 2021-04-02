import os
import csv
from datetime import datetime
import requests
from bs4 import BeautifulSoup


def requisicao_valor_nominal_atualizado():
    formdata = {
        'Data': '29032021',
        'escolha': '1',
        'Idioma': 'PT',
        'saida': 'xls',
        'Dt_Ref_Ver': '20210322',
        'Inicio': '29 / 03 / 2021'
    }
    from lxml import html

    html_response = requests.post('https://www.anbima.com.br/informacoes/vna/vna.asp', data=formdata)
    # soup = BeautifulSoup(html_response, 'html.parser')
    tree = html.fromstring(html_response.text)
    buyers = tree.xpath('//*[@id="listaLFT"]/center/table/tbody/tr[4]/td[2]')
    print(r.text)


def carregar_taxas_selic():
    taxas_selic = {}
    taxas_selic['dia'] = []
    taxas_selic['taxa'] = []

    with open(f'{os.path.dirname(__file__)}/../dados_externos/taxa_selic.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=';')
        for row in spamreader:
            dia = datetime.strptime(row[0], "%d/%m/%Y")
            taxa = float(row[1].replace(',', '.')) - 1
            taxas_selic['dia'].append(dia)
            taxas_selic['taxa'].append(taxa)

    return taxas_selic