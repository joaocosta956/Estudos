# Você precisa criar um programa em Python que conte a frequência de cada palavra em uma frase fornecida pelo usuário.
#  O programa deve ignorar a diferença entre letras maiúsculas e minúsculas e deve desconsiderar a pontuação.

import os
os.system('cls')

frase_input = input('Insira uma frase: ')

def separa_palavra(palavras):
    palavras_lista = []
    palavra = ''
    for letra in palavras:
        if letra != ' ' or '':
            palavra += letra
        else:
            palavras_lista.append(palavra)
            palavra = ''

    palavras_lista.append(palavra)
    print(palavras_lista)
    return palavras_lista


def contar_palavras_iguais(palavras_lista):
    palavra_salva = {}
    for palavra in palavras_lista:
        if palavra in palavra_salva:
            palavra_salva[palavra] += 1
        else:
            palavra_salva[palavra] = 1
    return(palavra_salva)



frase_1 = separa_palavra(frase_input)
frase_contagem = contar_palavras_iguais(frase_1)

for palavra, contagem in frase_contagem.items():
    print(f'Palavra: {palavra}, Contagem: {contagem}')