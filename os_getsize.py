import math
import os
from itertools import count


def formata_tamanho(num_tamanho: int, base: int = 1024):
    if num_tamanho <= 0:
        return '0B'

    abreviacao_tamanho = 'B', 'KB', 'MB', 'GB', 'TB', 'PB'

    indice_abreviacao_tamanho = int(math.log(num_tamanho, base))

    potencia = base ** indice_abreviacao_tamanho

    tamanho_final = num_tamanho / potencia

    abreviacao_tamanho = abreviacao_tamanho[indice_abreviacao_tamanho]

    return f'{tamanho_final:.2f} {abreviacao_tamanho}'


print(formata_tamanho(10000000))

caminho = "C:\\Users\\joaov\\Documents\\caminhos\\All"
counter = count()

for root, dirs, files in os.walk(caminho):
    the_counter = next(counter)
    print(the_counter, 'Pasta atual', root)

    for dir_ in dirs:
        print('  ', the_counter, 'Dir:', dir_)

    for file_ in files:
        caminho_completo_arquivo = os.path.join(root, file_)
        # tamanho = os.path.getsize(caminho_completo_arquivo)
        stats = os.stat(caminho_completo_arquivo)
        tamanho = stats.st_size
        print('  ', the_counter, 'FILE:', file_, formata_tamanho(tamanho))
