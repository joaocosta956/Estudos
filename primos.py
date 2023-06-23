
# Descobrir se é um número primo



print(30 * "-")     
print("Somento numeros inteiros, não negativos e menores 3!!!")
print(30 * "-")     
#  ----Cria um interface gráfica, afeta somente a estética do código------- 

numero = int(input("Insira um número para descobrir se o mesmo é primo: "))

#  A lógica aqui é que, todos números são divisiveis por 1, logo podemos pular esse número e prosseguir, indo logo para o 2 para
#  O número primo é um número natural, ou seja, não é negativo e é somente divisivel por 1 e por ele mesmo

if numero > 2:
    for x in range(2,numero):
        if(numero % x) == 0:
            print(f"O {numero} não é primo")
            break
        else:
            print(f"O {numero} é primo")
            break
else:
    print(30 * "-")
    print(f"O {numero} não é primo, ou o {numero} é menor ou igual a 2")