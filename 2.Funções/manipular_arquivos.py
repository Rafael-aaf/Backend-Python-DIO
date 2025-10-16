
""" Abrir e Fechar arquivos """

file = open("2.Funções/persuasion_ch1.txt", "r") # "r" -> read; "w" -> gravação; "a" -> anexar
file.close()

# Ler um arquivo - read, realine, readlines

file = open("2.Funções/persuasion_ch1.txt", "r", encoding="utf-8") # Precisa do encoding porque contêm caracteres especiais
#print(file.read())

#print(file.readline()) # Lê uma linha por vez

#for linha in file.readlines(): # Retorna uma lista. Ideal para iterar
#    print(linha)
file.close()


""" Escrever em um arquivo - write, writelines """

file = open("2.Funções/teste.txt", "w")
file.write("Oiii!")
file.writelines(["O", "i", "i", "i", "!"]) # Iterável
file.close()


""" Gerenciar arquivo e diretorio """

import os
import shutil
from pathlib import Path

ROOT_PATH = Path(__file__).parent # O pai do path desse arquivo

#os.mkdir(ROOT_PATH / 'novo') # Cria um diretório

arquivo = open(ROOT_PATH / "novo.txt", "w")
arquivo.close()

os.rename(ROOT_PATH / 'novo.txt', ROOT_PATH / "alterado.txt")

os.remove(ROOT_PATH / "alterado.txt")

#shutil.move(ROOT_PATH / "teste.txt", ROOT_PATH.parent) # Move arquivos

print('\n')

""" Tratamento de excessões """
from pathlib import Path

ROOT_PATH = Path(__file__).parent 

try:
    arquivo1 = open("meuarquivo.py", "r")
except FileNotFoundError as exc:
    print("Arquivo não encontrado!")
    print(exc)

try:
    arquivo2 = open("1.Introducao", "r")
except PermissionError as exc:
    print(f'Não foi possível abrir o arquivo: {exc}')

try:
    arquivo1 = open("meuarquivo.py", "r")
except FileNotFoundError as exc:
    print(f'Não foi possível abrir o arquivo: {exc}')
except PermissionError as exc:
    print(f'Não foi possível abrir o arquivo: {exc}')
except Exception as exc:
    print(f'Por algum motivo não foi possível abrir o arquivo: {exc}')


""" Boas Práticas """

# Usar 'with'! Ele usa um close() ao fim
# Certificar que o arquivo existe
# Usar a codificação correta - ex: utf-8, ascii
try:
    with open(ROOT_PATH / "persuasion_ch1.txt", "r", encoding='utf-8') as arquivo:
        print(arquivo.read())
except IOError as exc:
    print(exc)