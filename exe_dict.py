import os

os.system("cls")

perguntas = [
    {
        'Pergunta': 'Quanto é 2+2',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '2', #Indice
    },
    {
        'Pergunta': 'Quanto é 5*5',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '0', #Indice
    },
    {
        'Pergunta': 'Quanto é 10/2',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '1', #Indice
    },
]

for pergunta in perguntas:
    print('Pergunta:',pergunta['Pergunta'])
    print()

    for i, opcao in enumerate(pergunta['Opções']):
        print(f'{i})', opcao)
    print()

    escolha = input('Escolha uma opção: ')

    # escolha_int = None
    if escolha.isdigit():
        # escolha_int = int(escolha)
        if escolha == pergunta['Resposta']:
            print("Acertou")
        else:
            print("Errou")
    else:
        print('Você não digitou um numero')
    
