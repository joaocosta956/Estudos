import contas

class Pessoa:
    
    def __init__(self, nome : str, idade : int) -> None:
        self._nome = nome
        self._idade = idade

    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self,nome):
        self._nome = nome
        return self._nome
    
    @property
    def idade(self):
        return self._idade
    
    @idade.setter
    def idade(self,idade):
        self._idade = idade

    def __repr__(self) -> str:
        class_name = type(self).__name__
        attr = f'({self.nome!r}, {self.idade!r})'
        return f'{class_name},{attr}'
    
class Cliente(Pessoa):
    def __init__(self, nome: str, idade: int) -> None:
        super().__init__(nome, idade)
        self.conta : contas.Conta | None = None

if __name__ == '__main__':
    c1 = Cliente('Joao', 38)
    c1.conta = contas.ContaCorrente(112, 1300, 150, 100)
    print(c1.nome)
    print(c1.idade)
    print(c1.conta)
    c2 = Cliente('Maria', 18)
    c2.conta = contas.ContaPoupanca(111, 1500, 0)
    print(c2.nome)
    print(c2.idade)
    print(c2.conta)