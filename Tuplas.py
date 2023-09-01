# Tuplas são objetos em Python(assim como quase tudo), mas diferente das listas, elas não são mutáveis. Uma vez definida não tem como alterar

tupl = (1,2,3)

print(tupl)

# tupl[0] = 0 # O indice 0 é acessivel, mas não modificavél, para modificar teriamos que redefinir o valor que queremos alterar

tupl = (0,2,3) # Caso eu só definice o 0, ou seja tupl = (0), todos os números (1,2,3) seriam sobreescritos, ou seja, seriam perdidos

# As tuplas também podem conter todos tipos de dados/objetos.

tupla = (1,'2','três', True, 'Oi', 1.0, (1,2,3,'Olá'), ['Dentro','da','Lista'], {'num' : 12, 'nome' : 'Joao'})

print(10*'-','Usando print na tupla',10*'-')

print(tupla)

print(10*'-','Tupla com loop for',10*'-')

for i in tupla:
    print(i)

print(10*'-','Acessando os dados internos da tupla usando for',10*'-')

print(tupla[6])

for i in tupla[6]:
    print(i)

print(10*'-',10*'-')

for i in tupla[7]:
    print(i)

print(10*'-',10*'-')

print(tupla[8])

for i in tupla[8]:
    print('chave '+i)
    print(f'valor {tupla[8][i]}')

# Com tuplas podemos fazer algo bem comum nos programas em Python, chamado "packing-unpacking"
# É como se estivéssemos dizendo que "a e b são iguais a 0 e 'Deu certo?' respectivamente"
a,b = 0, 'Deu certo?'

print(10*'-','Packing-unpacking',10*'-')

print(a)
print(b)

# E podemos facilmente trocar os valores

a,b = b,a

print(10*'-',10*'-')

print(a)
print(b)