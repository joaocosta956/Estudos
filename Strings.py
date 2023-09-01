# Todas Strings em Python são iteraveis, ou seja, todas letras são endereçadas
# o que nos permite acessar por indice


#            0123456789.....
string_um = 'Olá, como você está?'

# Aqui nos podemos selecionar o inicio e o fim dos indices e também podemos selecinar de quantos em quantos
#               i:f  p
print(string_um[9:19:1])

# i = Inicio, f = Fim, p = Passos (Por padrão vem 1)
# Mas lembre-se, o a letra do 9, não vai aparecer, é apartir
# E caso não informe o index final, irá apartir do 9 até o fim.
print(10*'-','Passos 2',10*'-')
print(string_um[9::2])

# Se você colocar um número negativo a string é iterado ao contrário
# Não precisa informar os números
print(10*'-','Passos negativos -1',10*'-')
print(string_um[::-1])

# Agora veremos um palíndromo kkkk
palindromo = 'socorram me subi no onibus em marrocos'
print(10*'-','Palíndromo -1',10*'-')
print(palindromo[::-1])

# Aqui temos um loop while, poderia ser com for também
# Onde a função "len()" retorna o número de letras/indices
# Então enquanto len_string_um for menor que i (que começa no 0 e é incrementado no loop while)

len_string_um = len(string_um)
i = 0

print(10*'-','Por loop While',10*'-')

while i < len_string_um:
    print(string_um[i])
    i += 1
    print(f'Indice: {i}')

# Veja que até os espaços são mostrados
print(10*'-','Indices',10*'-')

print(string_um[0])
print(string_um[1])
print(string_um[2])
print(string_um[3])
print(string_um[4])
print(string_um[5])
print(string_um[6])
print(string_um[7])
print(string_um[8])
print(string_um[9])
print(string_um[10])
print(string_um[11])
print(string_um[12])
print(string_um[13])
print(string_um[14])
print(string_um[15])
print(string_um[16])
print(string_um[17])
print(string_um[18])
print(string_um[19])

# Vai até aqui, apartir daqui gera um Erro IndexError: string index out of range
# Ou seja o index da palavra está fora do "range", da "pool".
print(string_um[20])
