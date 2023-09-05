# Entradas de dados por parte do usuario são feitas com o input().
print(10*'-','Input',10*'-')

valor = input('Insira um valor: ')

# Porém, tenha em mente que todos os valores digitados pelo usuario serão strings.
# Mesmo que o usuario digite um número, o número será uma string, não um inteiro.

print(valor)

print(10*'-','Input números',10*'-')

numero = input('Insira um número: ')

# Existem diversas formas de verificar se o que foi digitado é realmente um número, mas é um passo mais complexo.

# Isto abaixo é um exemplo(bem mal feito), não precisa entender.
# IGNORE CASO NÃO ENTENDA.
while True:
#             Aqui é feito a verifação se tem ou não um número.
    if numero.isdigit():
        # Feito isto, o "numero" é convertido para um inteiro.
        numero = int(numero)
        i = 0
        while i < 11:
            i+=1
            print(i*numero)
        break
    else:
        print('O valor digitado não foi um número')
        numero = input('Insira um número: ')


# Uma outra forma é alterando diretamente o input, porém é bem sucetivel a erros, afinal não sabemos se o usuario ira inserir ou não um número, além de ficar mais dificil de encontrar o erro.

print(10*'-','Transformando str em int',10*'-')

numero = int(input('Insira um número: '))

print(numero+10)

# Outra forma é alterando depois do input(onde você pode tratar um erro).

print(10*'-','Input números',10*'-')

numero = input('Insira um numero: ')

numero = int(numero) # Fica mais legivel o que você quis fazer, além de ficar mais fácil a localização

print(numero*100)
