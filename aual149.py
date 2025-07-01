# Funções Decoradoras e decoradores com classe

def add_repr(class_):
    def my_repr(self):
        class_name = self.__class__.__name__
        class_dict = self.__dict__
        class_repr = f'({class_name},{class_dict})'
        return class_repr
    class_.__repr__ = my_repr
    return class_

@add_repr
class Time:
    def __init__(self, nome):
        self.nome = nome

@add_repr
class Planeta:
    def __init__(self, nome):
        self.nome = nome

# Time = add_repr(Time)  Ao inves de fazer assim, adiciona Sintax Sugar

brasil = Time('Brasil')
planeta = Planeta('Terra')

print(brasil)
print(planeta)