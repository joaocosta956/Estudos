import os

palavra = "arroz"
print(f"A palavra tem {len(palavra)} letras")
print("Tente advinhar a palavra secreta.")
print("-"*30)
letra_acertada =''
numero_tentativas = 0

while True:
    inp_user = input("Digite uma letra: ")
    numero_tentativas += 1
    if len(inp_user) > 1:
        print("Válido apenas um digito!")
        continue

    if inp_user in palavra:
        letra_acertada += inp_user

    palavra_formada = ''
    for letra_secret in palavra:
        if letra_secret in letra_acertada:
            palavra_formada += letra_secret
        else:
            palavra_formada += "*"
    print(palavra_formada)

    if palavra_formada == palavra:
        os.system('cls')
        print("Você acertou!!")
        print("Número de tentativas: ",numero_tentativas)
        letra_acertada =''
        numero_tentativas = 0
        break