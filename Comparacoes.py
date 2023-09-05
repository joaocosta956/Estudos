# Temos três operadores de comparação:
# O if : se "x" for verdade, faça algo
# o elif : Senão, se "y" for verdade, faça algo
# E o else : Caso não, faça outra coisa

# Exemplo:

x = 10
y = 5

print(10*'-','If, Elif, Else',10*'-')

# Se X for maior que Y, faça.
if x > y:
    print(f'{x} é maior que {y}')

# Caso não seja maior, verifica se não é igual e então faça
elif x == y:
    print(f'{x} é igual a {y}')

# Caso não seja nenhuma das opções, faça isto
else:
    print(f'{x} é menor que {y}')



# Podemos deixar isto interativo


print(10*'-','Usando input',10*'-')

y = int(input('Insira um valor: '))

# Se X for maior que Y, faça
if x > y:
    print(f'{x} é maior que {y}')

# Caso não seja maior, verifica se não é igual
elif x == y:
    print(f'{x} é igual a {y}')

# Caso não seja nenhuma das opções, faça isto
else:
    print(f'{x} é menor que {y}')

# Assim são feitos algoritimos de comparação

