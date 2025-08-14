# os.walk para navegar de caminhos de forma recursiva
# os.walk é uma função que permite percorrer uma estrutura de diretórios de
# maneira recursiva. Ela gera uma sequência de tuplas, onde cada tupla possui
# três elementos: o diretório atual (root), uma lista de subdiretórios (dirs)
# e uma lista dos arquivos do diretório atual (files).


# D:\SteamLibrary\steamapps\common\Grand Theft Auto San Andreas
import os
from itertools import count

os.system('cls')

path = os.path.join('D:', 'SteamLibrary', 'steamapps',
                    'common', 'Grand Theft Auto San Andreas')

path = r'D:\\SteamLibrary\\steamapps\\common\\Grand Theft Auto San Andreas'
counter = count()


for root, dirs, archive in os.walk(path):
    the_counter = next(counter)
    print(the_counter, root)

    for dir_ in dirs:
        print('     Pasta', the_counter, dir_)

    for file_ in archive:
        print('     Arquivo', the_counter, file_)
