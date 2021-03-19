import numpy as np
import csv
import os
from datetime import datetime, timedelta


def adicionar_dias_uteis(data, dias):
    nova_data = adicionar_dias_corridos(data=data, dias=dias)

    while not np.is_busday(dates=nova_data, weekmask='1111100', holidays=holidays):
        nova_data = adicionar_dias_corridos(data=nova_data, dias=1)

    return nova_data


def remover_dias_uteis(data, dias):
    nova_data = remover_dias_corridos(data=data, dias=dias)

    while not np.is_busday(dates=nova_data, weekmask='1111100', holidays=holidays):
        nova_data = remover_dias_corridos(data=nova_data, dias=1)

    return nova_data


def adicionar_dias_corridos(data, dias):
    nova_data = datetime.strptime(data, "%Y-%m-%d") + timedelta(days=dias)
    return nova_data.strftime("%Y-%m-%d")


def remover_dias_corridos(data, dias):
    nova_data = datetime.strptime(data, "%Y-%m-%d") - timedelta(days=dias)
    return nova_data.strftime("%Y-%m-%d")


def coverte_formato_data(data):
    return f'{data[-4:]}-{data[3:5]}-{data[:2]}'


def calcula_dias_uteis(data_inicio, data_fim):
    return np.busday_count(begindates=data_inicio, enddates=data_fim, weekmask='1111100', holidays=holidays)


def carregar_feriados():
    holidays = []
    with open(f'{os.path.dirname(__file__)}/../data/feriados_nacionais.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=';')
        for row in spamreader:
            holidays.append(coverte_formato_data(data=row[0]))

    return holidays


holidays = carregar_feriados()
