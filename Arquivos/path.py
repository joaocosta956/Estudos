# os.walk para navegar de caminhos de forma recursiva
# os.walk é uma função que permite percorrer uma estrutura de diretórios de
# maneira recursiva. Ela gera uma sequência de tuplas, onde cada tupla possui
# três elementos: o diretório atual (root), uma lista de subdiretórios (dirs)
# e uma lista dos arquivos do diretório atual (files).


import math
# D:\SteamLibrary\steamapps\common\Grand Theft Auto San Andreas
import os
from itertools import count


def formata_tamanho(tamanho_em_bytes: int, base: int = 1000) -> str:
    """Formata um tamanho, de bytes para o tamanho apropriado"""

    # Original:
    # https://stackoverflow.com/questions/5194057/better-way-to-convert-file-sizes-in-python

    # Se o tamanho for menor ou igual a 0, 0B.
    if tamanho_em_bytes <= 0:
        return "0B"

    # Tupla com os tamanhos
    #                      0    1     2     3     4     5
    abreviacao_tamanhos = "B", "KB", "MB", "GB", "TB", "PB"
    # Logaritmo -> https://brasilescola.uol.com.br/matematica/logaritmo.htm
    # math.log vai retornar o logaritmo do tamanho_em_bytes
    # com a base (1000 por padrão), isso deve bater
    # com o nosso índice na abreviação dos tamanhos
    indice_abreviacao_tamanhos = int(math.log(tamanho_em_bytes, base))
    # Por quanto nosso tamanho deve ser dividido para
    # gerar o tamanho correto.
    potencia = base ** indice_abreviacao_tamanhos
    # Nosso tamanho final
    tamanho_final = tamanho_em_bytes / potencia
    # A abreviação que queremos
    abreviacao_tamanho = abreviacao_tamanhos[indice_abreviacao_tamanhos]
    return f'{tamanho_final:.2f} {abreviacao_tamanho}'


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
        caminho_completo = os.path.join(root, file_)
        tamanho_arquivo = os.path.getsize(caminho_completo)
        print('     Arquivo', the_counter, file_,
              formata_tamanho(tamanho_arquivo))
        print('     Arquivo', the_counter, file_,
              formata_tamanho(tamanho_arquivo))
