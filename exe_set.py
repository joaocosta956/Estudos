lista_inteiros = [
    [1, 2, 3, 3, 2, 1],
    [2, 3, 4, 1, 2, 3],
    [2, 3, 6, 7, 5, 3],
    [5, 5, 7, 8, 9, 9],
]

# função que encontra o primeiro numero duplicado
def encontra_prim_num_dup(lista_int):
    numeros_checados = set()
    primeiro_duplicado = -1

    for numero in lista_int:
        if numero in numeros_checados:
            primeiro_duplicado = numero
            break
        numeros_checados.add(numero)
    
    
    print()
    print()
    return primeiro_duplicado

for lista in lista_inteiros:
    print(lista, encontra_prim_num_dup(lista))

























"""------------------------------- minha tentativaksksks

len = len(lista_inteiros)

numero_ind = 0
numero_salvo = 9

for num in lista_inteiros[numero_ind]:
    # print(num)
    if num == numero_salvo:    
        print(numero_salvo)
        break
    numero_ind += 1
    numero_salvo = num








# for numero_ind in len:
#     print(lista_inteiros[numero_ind]) 
#     numero_ind += 1
    # for len in lista_inteiros:
    #     print(lista_inteiros[len])

# s3 = tuple(lista_inteiros)
# print(s3)
# s2 = set(s3)
# s1 = set(s2)

# for i in lista_inteiros:
#     s1.add(i)
#     print(s1)



"""