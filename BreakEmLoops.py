# O comando Break serve para encerrar um laço de while e for

print(10*'-','Break em um loop for',10*'-')

# n = int(input('Insira um número: '))

# for i in range(2, n):
#     if n % i == 0:
#         print('Número não é primo')     
#     else:
#         print('Não é primo')
#     break # Tente apagar este linha para ver o que acontece


print(10*'-','Break em loop while',10*'-')

b = 0

while True: # Loop infinito
    b+=1
    print(b)
    if b > 10: break # Se após o ":" houver pouquissimas linhas, podemos deixar o código inline

print(10*'-','Break em while aninhado',10*'-')

while True:
    a = 0
    while True:
        a+=1
        print(a)
        if a > 5: break # Cancela somente o loop interno
    
    print('loop interno quebrado')
    break

