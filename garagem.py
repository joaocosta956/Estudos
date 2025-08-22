# Sistema de garagem de carro
# Precisa ter placa, nome do carro, marca do carro
# Sistema de consulta por placa
# Criar primeiro uma instância da Classe Carro para depois poder adicionar
# parametros
# Verfica se todos requisitos foram preenchidos (Coloquei bool, mas poderia ser
# None)

from os import system

system('cls')


class Carro:
    ...


placas = {
    'AAAA1': ['Civic', 'Honda'],

}


def terminal_clean():
    system('cls')


def consulta_placa():
    placa = input('\nIsira o número da placa: ').upper()
    if placa in placas:
        for x in placas[placa]:
            print(x)
    else:
        print('Não há esta placa!')


def adiciona_placa():
    # Parametros definidos dentro da função via input, mas poderia coletar
    # fora também, fiz assim pois evita bastante if's
    modelo = input('Insira o modelo do carro: ')
    marca = input('Insira a marca do carro: ')
    placa = input('Insira a placa: ')
    if modelo and marca and placa:
        placa = placa.upper().strip()
        placas[placa] = [modelo, marca]


def consulta_todas():
    for x in placas:
        print(x, placas[x])


def check_opcao(opcao: str):
    if opcao in opcoes:
        opcoes[opcao]()
    else:
        print('Digite uma das letras informadas.')


# Aqui só funciona com funções!!!!!
opcoes = {
    'I': adiciona_placa,
    'C': consulta_placa,
    'L': terminal_clean,
    'A': consulta_todas,
    '': ...,
    '': ...,
    '': ...,
}

mensagem = f'\n{10*"-"}[I]Inserir [C]Consultar [S]Sair [L]Limpar {10*"-"}'

if __name__ == "__main__":
    while True:
        print(mensagem)
        opcao = input('Insira o comando: ').upper()
        check_opcao(opcao)

        # info = {
        #     'PLACA': False,
        #     'CARRO': False,
        #     'MARCA': False,

        # }
        # print(info)
        # for x in info:
        #     a = input('TRUE')

        #     info[x] = True
        #     print(info)
