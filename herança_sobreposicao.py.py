

# Herdamos a classe str(nativa do Python) na classe Foo e sobreescrevemos o metodo upper(), e demos um retorno com super() para o metodo pela classe
# pai(str)


# class Foo(str):
#     def upper(self):
#         print('Dentro Upper')
#         retorno = super().upper()
#         print('Depois do Upper')
#         return retorno
    
# string = Foo('eita')

# print(string.upper())


class A:
    atributo_a = 'valor a'

    def __init__(self, parametro): #__init__ sobreescrito pelo __init__ da classe B
        self.parametro = parametro

    def metodo(self):
        print('A')



class B(A):
    atributo_b = 'valor b'

    def __init__(self, parametro, outra_coisa): #posso receber outro parametro sem interferir no anterior
        super().__init__(parametro)
        self.outra_coisa = outra_coisa

    def metodo(self):
        super().metodo()
        print('B')

class C(B):

    atributo_c = 'valor c'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print('Agora eu posso fazer outra coisa sem me preocupar com os argumentos!!')

    def metodo(self):
        super(C, self).metodo() 
        print('C')
        #super() não precisa dos argumentos, apenas para demonstrar ;)



# print(C.mro()) #Method Resolution Order
print_c = C('Ola', 'Outra coisa') # São obrigatórios dois argumentos por causa das outras classes
print_c.metodo()