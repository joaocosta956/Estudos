# Código simples para criptografia básica, falta muito tratamento ainda, como valores inteiros


chave = input("Digite a palavra chave: ")


#Aqui ficam todas as substituições
substituicoes = {
    'A': '@',
    'a': '@',
    'B': '11',
    'b': '11',
    'C': '12',
    'c': '12',
    'D': '13',
    'd': '13',
    'E': '3',
    'e': '3',
    'F': '15',
    'f': '15',
    'I': '/',
    'i': '/',
    'O': '0',
    'o': '0',
    'U': '*',
    'u': '*'
}


#Aqui é onde a senha será salva
senha = ""

#Aqui fica a lógica
#Para cada letra na variavel "chave", verifica se a letra(variavel que vai armazenar todas as letras da variavel chave) está no dicionário "substituições", caso esteja, nós acrescentamos ela na variavel que vai guardar a senha gerada, a substituição é feita por Chave, e retorna o valor. Exemplo: letra = A, senha += substituições[A] -> que retorna @.
#Caso contrário, só adicione a letra a variavel "senha".
for letra in chave:
    if letra in substituicoes:
        senha += substituicoes[letra]
    else:
        senha += letra

print(senha)
