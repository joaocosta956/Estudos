class Caneta:
    def __init__(self, cor : str):
        self.cor_tinta = cor

    @property
    def cor(self):
        return self.cor_tinta
    

bic_azul = Caneta('Azul')

print(bic_azul.cor)