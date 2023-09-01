# Listas podem conter praticamente todos tipos de dados (tuple, int, str, float, list, dict ....)

lista_1 = [1,'2', 'três', True, ['oi', 2], (1,2,3,4)]

print(10*'-','Tudo presente na lista',10*'-')

print(lista_1[0])
print(lista_1[1])
print(lista_1[2])
print(lista_1[3])
print(lista_1[4])
print(lista_1[4][0]) # Podemos acessar os indices dos iteraveis
print(lista_1[4][1])
print(lista_1[5])
print(lista_1[5][0]) # O mesmo aqui
print(lista_1[5][1])
print(lista_1[5][2])
print(lista_1[5][3])


# Podemos somar números ou concatenar palavras (ATENÇÃO!!!------- Procure sempre deixar a lista limpa, ou seja, se tem inteiros, será só inteiros, pois se não irá gerar um erro!!!)
# Não podemos somar palavras sem concatenar números(somente se forem strings)

lista_2 = [0,1,2,3,4,5,6]
lista_3 = ['Olá', 'como', 'você', 'está?']

print(10*'-','Somas e concatenações',10*'-')

print(lista_2[1]+lista_2[6])
print(lista_3[0]+lista_3[1]+lista_3[2],lista_3[3]) # Perceba que ficou tudo colado, mas isto pode ser fácilmente corrigo adicionando um espaço(sim, em Python espaços são dados válidos)
# print(lista_2[1]+lista_3[0]) # Isto irá gerar um erro, por não podermos somar ou unir inteiros com strings

# Também podemos pegar a lista de trás para frente, colocando números negativos

#         -7 -6 -5 -4 -3 -2 -1
lista_2 = [0, 1, 2, 3, 4, 5, 6]

print(10*'-','De trás para frente',10*'-')

print(lista_2[-1], lista_2[-3])
print(lista_2[2:-1])

# Podemos saber o tamanho de uma lista com o len()

print(10*'-','Tamanho da lista',10*'-')

print(len(lista_2)) # -> 7 indices

# Uma caracteristica importando das listas é que elas são mutaveis(diferente de tuplas e strings)

print(10*'-','Listas mutáveis',10*'-')

lista_3[0] = 'Oi'

print(lista_3[0])

lista_2[0] = lista_2[4]+lista_2[4]

print(lista_2[0])

print(10*'-','Aplicação interessante de listas',10*'-')

matriz = [lista_1, lista_2, lista_3]
print(matriz)