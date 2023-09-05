# For é uma ferramente poderosa e caraterística desta linguagem. Com for, podemos varrer qualquer sequencia (strings, listas, tuplas) ou dicionário.

print(10*'-','Usando For',10*'-')

lista = ['João', 'Gustavo', 'Bruno']

#   i é o nome da variavel onde serão armazenados os valores.
for i in lista:
    print(f'i agora é {i}')
    print(f'{i} tem {len(i)} letras')

print(20*'-')

# O nome da variavel pode ser qualquer um, por exemplo "batata"
for batata in lista:
    print(f'batata agora é {batata}')
    print(f'{batata} tem {len(batata)} letras')


# Uma função importante para usarmos o for é a função range(ni,nf,i), que cria um lista começando
# do inteiro ni até o inteiro nf-1, com incremento i entre os números

print(10*'-','Usando Range',10*'-')

print(list(range(1,12,2)))
print(list(range(10))) # Podemos omitir o inicio e o incremento
print(list(range(5, 15)))

# Sinceramente eu não sei explicar o porque temos que converter para uma lista, só sei que temos :)
# No Python vários retornos não são o que a gente espera, então temos que trata-los antes de usa-los

intervalo = range(1, 21)

for bruh in intervalo:
    print(bruh**2)

# Usando range e for

print(10*'-','Usando For e Range',10*'-')

for i in range(len(lista)):
    print(i,lista[i])

# Aqui vemos porque é interessante que range gere uma lista de números inteiros

matriz = ((1,0,0),(0,1,0),(0,0,1))

print(matriz)

for i in range(len(matriz)): # Verifica quantos indices tem na matriz, a tupla externa ou pai
    print('\n')
    for j in range(len(matriz[i])): # Aqui verifica quantos indices tem na tupla interna/filho(a)
        print(matriz[i][j])


print(10*'-','Usando For em Dicionários',10*'-')

# No caso de dicionário, o for pega a chave e não um inteiro

orcamento = {'combustivel':200, 'motor':4500, 'oleo':500}

for seila in orcamento:
    print(seila)

print(20*'-')

# Assim podemos acessar os valores internos

for valor in orcamento:
    print(f'É igual fazer orcamento[{valor}], mas de forma dinâmica')
    print(f'{valor} custa R${orcamento[valor]}')
    print('\n'*2)
