import csv
from pathlib import Path

ROOT_PATH = Path(__file__).parent 

""" Cria e Escreve o arquivo csv
try:
    with open(ROOT_PATH / 'usuarios.csv', "w", encoding="utf-8", newline="") as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow(['id', 'nome'])
        escritor.writerow(['1', 'Anna'])
        escritor.writerow(['2', 'Rafael'])
except IOError as exc:
    print(f'Erro ao criar arquivo: {exc}')
"""

# Ler o arquivo
try:
    with open(ROOT_PATH / 'usuarios.csv', "r", encoding="utf-8", newline="") as arquivo:
        leitor = csv.reader(arquivo)
        for row in leitor:
            print(','.join(row))
except IOError as exc:
    print(f'Erro ao criar arquivo: {exc}')