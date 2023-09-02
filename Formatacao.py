# Podemos formatar as strings que serão mostradas

nome = 'Gustavo'
idade = 24

# Neste caso armazenei a mensagem em uma variavel de mesmo nome.
# Utilizei o .format() no final da mensagem, colocando as variaveis que quero mostrar em ordem

mensagem = 'Olá, {}.Você tem {} anos.'.format(nome, idade)

print(10*'-','Utilizando .format()',10*'-')

print(mensagem)

# Outra forma é uma que já utilizei e utilizo em outros arquivos
# Na minha opinão, a melhor forma

mensagem = f'Olá, {nome}. Você tem {idade} anos'

print(10*'-','Utilizando f-strings',10*'-')

print(mensagem)

# Formatação de números

preco = 19.99

# O número antes do "f" indica quantos números após a virgula

mensagem = f'O preço é: R${preco:.1f}'

print(10*'-','Formatando números',10*'-')

print(mensagem)