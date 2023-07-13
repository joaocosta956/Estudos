import os

lista = []

while True:
    print('Selecione uma opção')
    opcao = input('[i]inserir [a]apagar [l]listar: ')

    if opcao.lower() == 'i':
        os.system('cls')
        valor = input('Valor: ')
        lista.append(valor)
    elif opcao.lower() == 'a':
        indice_str = input('Escolha o indice a apagar: ')
        
        try:
            indice = int(indice_str)
            del lista[indice]
        except:
            print('Não foi possivel apagar este indice!')
    
    elif opcao.lower() == 'l':
        os.system('cls')
    
        if len(lista) == 0:
            print('Lista vazia')
        
        for i, valor in enumerate(lista):
            print(i, valor)