class Carro:
    def __init__(self,nome):
        self.nome = nome
        self._motor = None
        self._fabricante = None

    @property
    def motor(self):
        return self._motor

    @motor.setter
    def motor(self, valor):
        self._motor = valor

    @property
    def fabricante(self):
        return self._fabricante

    @fabricante.setter
    def fabricante(self, valor):
        self._fabricante = valor



class Motor:
    def __init__(self,nome):
        self.nome = nome



class Fabricante:
    def __init__(self,nome):
        self.nome = nome


carro1 = Carro('Fusca')
volkswagem = Fabricante('Volkswagem')
motor_1 = Motor('1.0')
carro1.fabricante = volkswagem
carro1.motor = motor_1

#print(carro1.fabricante.nome,carro1.nome,carro1.motor.nome)

uno = Carro('Uno')
fiat = Fabricante('Fiat')
uno.fabricante = fiat
uno.motor = motor_1

#print(uno.fabricante.nome,uno.nome,uno.motor.nome )

focus = Carro('Focus')
ford = Fabricante('Ford')
motor_2 = Motor('2.0')
focus.fabricante = ford
focus.motor = motor_2

#print(focus.fabricante.nome,focus.nome,focus.motor.nome)

def get_dados(carro):
    print(carro.nome, carro.fabricante.nome, carro.motor.nome)

get_dados(uno)
get_dados(focus)
get_dados(carro1)
