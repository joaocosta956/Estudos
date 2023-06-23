# Código simples para criptografia básica, falta muito tratamento ainda, como valores inteiros


chave = input("Digite a palavra chave: ")

substituicoes = {
    'A': '@',
    'a': '@',
    'B': '11',
    'b': '11',
    'C': '12',
    'c': '12',
    'D': '13',
    'd': '13',
    'E': '3',
    'e': '3',
    'F': '15',
    'f': '15',
    'I': '/',
    'i': '/',
    'O': '0',
    'o': '0',
    'U': '*',
    'u': '*'
}

senha = ""
for letra in chave:
    if letra in substituicoes:
        senha += substituicoes[letra]
    else:
        senha += letra

print(senha)