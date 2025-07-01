class Caneta:
    def __init__(self,cor: str):
        # Private Protect
        # Este atributo é exclusivo da classe, utilize usando o getter
        self._cor = cor


    # Getter, evita que o código cliente quebre
    @property
    def cor(self):
        return self._cor
    
    @cor.setter
    def cor(self, valor):
        print('Alterando cor...')
        if isinstance(valor,int):
            raise ValueError('Não aceito numeros')
        self._cor = valor

caneta = Caneta('Azul')

print(caneta.cor)
caneta.cor = 'Rosa'
print(caneta.cor)
caneta.cor = 123
print(caneta.cor)