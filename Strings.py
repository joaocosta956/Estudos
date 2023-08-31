# Todas Strings em Python são iteraveis, ou seja, todas letras são endereçadas
# o que nos permite acessar por indice


#            0123456789.....
string_um = 'Olá, como você está?'

# Veja que até os espaços são mostrados

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

