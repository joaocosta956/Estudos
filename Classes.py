class Camera:
    def __init__(self, nome, filmando=False):
        self.nome = nome
        self.filmando = filmando

    def filmar(self):
        if self.filmando:
            print(f'{self.nome} já está filmando...')
            return
        print(f'{self.nome} está filmando...')
        filmando = True

    def parar_filmar(self):
        if not self.filmando:
            print(f'{self.nome} não esta filmando...')
            return
        
        print(f'{self.nome} parando de filmar...')
        self.filmando = False



    def fotografar(self):
        if self.filmando:
            print(f'{self.nome} não pode fotografar por estar filmando...')
            return
        
        print(f'{self.nome} camera fotografando')

c1 = Camera('Canon')
c2 = Camera('Sony')

c1.filmar()
print(c1.filmando)
print(c2.filmando)