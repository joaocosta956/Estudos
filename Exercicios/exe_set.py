lista_inteiros = [
    [1, 2, 3, 3, 2, 1],
    [2, 3, 4, 1, 2, 3],
    [2, 3, 6, 7, 5, 3],
    [5, 5, 7, 8, 9, 9],
]

#função que encontra o primeiro numero duplicado
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
