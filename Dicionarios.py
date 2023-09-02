# Dicionarios são um pouco mais complexos, pois não são sequências e nem sequenciados/iteraveis como strings, tuplas, listas.
# São indereçados por chaves, cada chave com seu valor, caso queira saber os valores, terá que primeiro saber as chaves.

# Podemos colocar diversos valores, inclusive dicionarios dentro de dicionarios(bem mais avançado), ou mesmo listas dentro de dicionarios e vice versa.
# Procure sempre ser claro com as chaves e valores, se eu tenho uma chave "nome", não pode ter um inteiro nela.
# E sempre deixe uma virgula "," no final, porque dicionarios podem ser incrementados.
pessoa = {
    'nome' : 'Joao',
    'profissão' : 'programador',
    'idade' : 18,
    'trabalha' : False, #lol
}

# Podemos pegar chaves e valores de diversas formas.

chaves = pessoa.keys() # Retorna uma lista com as chaves.
valores = pessoa.values() # Retorna uma lista com os valores.

print(10*'-','pessoa.keys() e pessoa.values()',10*'-')

print(chaves)
print(valores)

# Com iteração por chaves e valores com o loop for
print(10*'-','Com loop for simples',10*'-')

for chave in pessoa:
    valor = pessoa[chave]
    print(f'Chave: {chave} \nValor: {valor}')

# Com o método 'items()' que retorna uma tupla com os dois valores, chave e valor.

print(10*'-','Com método "items()"',10*'-')

for chave, valor in pessoa.items():
    print(f'Chave: {chave} \nValor: {valor}')

# Podemos adicionar mais valores e chaves.

print(10*'-','Adicionando novos valores',10*'-')

pessoa['trabalha'] = True

print(pessoa['trabalha'])

print(10*'-','Adicionando novas chaves',10*'-')

pessoa['renda'] = 1000

print(pessoa['renda'])

# Por conta dos dicionários serem mutáveis, podemos facilmente alterar os valores contidos.

print(10*'-','Modificando valores',10*'-')

pessoa['renda'] = pessoa['renda']+500

print(pessoa['renda'])


# Podemos perguntar se o dicionario contém uma chave especifica.
# Nas versões anteriores do Python se possuía o método .has_key, porém não é mais utilizado.

# pessoa.has_key('idade')
# pessoa.has_key('região')

# Mas nós ainda podemos fazer esta verficação com if's.

print(10*'-','"in" e "not in" para descobri chaves',10*'-')

if 'idade' in pessoa:
    print('A chave existe neste dicionário')

if 'região' not in pessoa:
    print('A chave não existe neste dicionário')

# Utilizei o 'in' e o 'not in' como exemplo, o correto é usar apenas um e retornar(caso falso) com "else".
# E por favor, coloque as strings em uma variavel, caso contrario você irá sofrer muito em futuras manutenções.
