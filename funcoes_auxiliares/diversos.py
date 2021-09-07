import os
import csv
from datetime import datetime


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