import pessoa
import contas

class Banco:
    def __init__(self, agencia : list[int] | None = None, cliente : list[pessoa.Pessoa] | None = None,
                conta : list[contas.Conta] | None = None) -> None:
        
        self.agencia = agencia or []
        self.cliente = cliente or []
        self.conta = conta or []


    def __repr__(self) -> str:
        class_name = type(self).__name__
        attr = f'({self.agencia!r}, {self.cliente!r}, {self.conta})'
        return f'{class_name},{attr}'

    def _check_conta(self,conta):
        if conta.conta in self.conta:
            return True
        print('conta')
        return False

    def _check_agencia(self,conta):
        if conta.agencia in self.agencia:
            return True
        print('agencia')
        return False

    def _check_cliente(self,cliente):
        if cliente in self.cliente:
            return True
        print('cliente')
        return False
    
    def autenticar(self, conta, cliente):
        return self._check_agencia(conta) and \
        self._check_cliente(cliente) and \
        self._check_conta(conta)
    


if __name__ == '__main__':
    c1 = pessoa.Cliente('Joao', 38)
    c1.conta = contas.ContaCorrente(112, 1300, 150, 100)
    print(c1.nome)
    print(c1.idade)
    print(c1.conta)
    c2 = pessoa.Cliente('Maria', 18)
    c2.conta = contas.ContaPoupanca(111, 1500, 0)
    print(c2.nome)
    print(c2.idade)
    print(c2.conta)

    banco = Banco()
    banco.cliente.extend([c1,c2])
    banco.conta.extend([c1.conta.conta,c2.conta.conta])
    banco.agencia.extend([111,222])
    print(banco)

    print(banco.autenticar(c1.conta, c1))
    print(banco.autenticar(c2.conta, c2))