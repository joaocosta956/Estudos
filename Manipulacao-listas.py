# Append, adiciona um valor(qualquer valor, int, str, etc) ao final da lista

lista1 = [1, 2, 3, 4, 5]

print(10*'-','Append',10*'-')

print('Antes do append',10*'-')
print(lista1)

lista1.append(6)

print('Depois do append',10*'-')
print(lista1)

# Extend, faz a mesma coisa que o Append, mas com listas

extencao1 = [1, 'Olá', True, 10.3]
lista1.extend(extencao1)

print(10*'-','Extend',10*'-')
print(f'O que eu quero extender {extencao1}')
print(lista1)

# Caso coloquemos com Append, será colocado como uma lista interna

lista2 = ['Lista externa', 1, 2]

print(10*'-','Extenção com Append',10*'-')
lista2.append(['Lista interna', extencao1]) # As listas ocupam um único indice

i=0
for valor in lista2:
    print(f'Indice: {i} Valor: {valor}')
    i+=1

# Usando o insert, insert serve para inserir um valor em um indice especifico

print(10*'-','Insert',10*'-')
#           indice,valor
lista1.insert(0,'Inicio')
lista1.insert(2,'Olá')

print(lista1)

# Usando o remove, remove serve para remover um valor especifico

print(10*'-','Remove',10*'-')
lista1.remove('Inicio')
print(lista1)

# Usando o pop, pop remove um valor por indice e o retorna(muito útil para projetos que envolvem listas)

print(10*'-','Pop',10*'-')
print(f'Valor removido: {lista1.pop(0)}')
print(lista1)

# Usando o count, ele retorna quantas vezes seu argumento aparace na lista

print(10*'-','Count',10*'-')
print(f'O valor se repete: {lista1.count(1)}')

# Varredura ao contrario

numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

print(10*'-','Varredura ao contrário',10*'-')
print(numeros[::-1])