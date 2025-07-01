import abc

class Conta(abc.ABC):
    def __init__(self, agencia : int, conta : int , saldo=0):
        self._agencia = agencia
        self._conta = conta
        self._saldo = saldo

    @abc.abstractmethod
    def sacar(self,valor : int):
        ...

    @property
    def agencia(self):
        return self._agencia
    @agencia.setter
    def agencia(self, value):
        self._agencia = value

    @property
    def conta(self):
        return self._conta
    @conta.setter
    def conta(self, value):
        self._conta = value

    @property
    def saldo(self):
        return self._saldo
    @saldo.setter
    def saldo(self, value):
        self._saldo = value

    def depositar(self, valor : int):
        self.saldo += valor
        self.detalhes(f'(Deposito {valor})')

    def detalhes(self, msg=''):
        print(f'O seu saldo é {self.saldo:.2f} -> {msg}')

    def __repr__(self) -> str:
        class_name = type(self).__name__
        attr = f'({self.agencia!r}, {self.conta!r}, {self.saldo})'
        return f'{class_name},{attr}'


class ContaPoupanca(Conta):

    def sacar(self, valor):
        saldo_pos_saque = self.saldo - valor

        if saldo_pos_saque >= 0:
            self.saldo -= valor
            self.detalhes(f'SAQUE {valor}')
            return valor
        print('Não foi possivel sacar o valor desejado')
        self.detalhes(f'SAQUE NEGADO {valor}')

class ContaCorrente(Conta):
    def __init__(self, agencia, conta, saldo=0, limite=0):
        super().__init__(agencia,conta, saldo)
        self._limite = limite

    def __repr__(self) -> str:
        class_name = type(self).__name__
        attr = f'({self.agencia!r}, {self.conta!r}, {self.saldo}, {self.limite})'
        return f'{class_name},{attr}'

    @property
    def limite(self):
        return self._limite
    @limite.setter
    def agencia(self, value):
        self._limite = value

    def sacar(self, valor):
        saldo_pos_saque = self.saldo - valor
        limite_maximo = self.limite
        if saldo_pos_saque >= limite_maximo:
            self.saldo -= valor
            self.detalhes(f'SAQUE {valor}')
            return valor
        print('Não foi possivel sacar o valor desejado')
        self.detalhes(f'SAQUE NEGADO {valor}')

if __name__ == '__main__':
    cp1 = ContaPoupanca(111,202,10)
    cp1.sacar(15)
    cp1.depositar(5)
    cp1.sacar(14)
    cc1 = ContaCorrente(111,202,10, -100)
    cc1.sacar(15)
    cc1.depositar(5)
    cc1.sacar(14)