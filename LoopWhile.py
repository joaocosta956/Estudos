# While, fica em loop até determinada condição ser falsa
# Cuidado com loops While, caso defina uma condição que sempre será verdadeira, esse loop sempre vai existir, se sempre existir, sempre será executado, o que com certeza vai consumir processamento, memoria e consequentemente lentidão

print(10*'-','While',10*'-')

# i tem valor 0
i = 0

# Lembre-se que, caso coloque a variavel i = 0 dentro do loop, irá gerar um loop infinito, tenha isto em mente, sempre.
while i < 5:
    # Se definissemos a variavel i aqui, ela sempre seria 0, consequentemente, a condição é sempre verdadeira
    # Muito cuidado com loops infinitos, em terminais é só dar Ctrl/Command + C que isto irá matar o terminal
    print(i)
    i+=1

print(10*'-','While mais complexo',10*'-')

i = 0

while i < 5 :
    print('{} dólar valem {} reais'.format(i, i*4,98))
    i+=1