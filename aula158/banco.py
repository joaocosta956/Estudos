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
        if conta in self.conta:
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
    
    # Importante ter porque se um cliente estiver cadastrado e ele colocar uma conta de outro cliente,
    # por exemplo, c1 não tem saldo, mas a c2 tem, poderia colocar a c1 com a conta da c2 e passaria pela
    # autenticação
    def check_acc(self, conta, cliente):
        if conta is cliente.conta:
            return True
        return False
    
    def autenticar(self, conta : contas.Conta, cliente : pessoa.Cliente):
        return self._check_agencia(conta) and \
        self._check_cliente(cliente) and \
        self._check_conta(conta) and self.check_acc(conta, cliente)
    


if __name__ == '__main__':
    c1 = pessoa.Cliente('Joao', 38)
    c1.conta = contas.ContaCorrente(112, 1300, 150, 100)
    # print(c1.nome)
    # print(c1.idade)
    c2 = pessoa.Cliente('Maria', 18)
    c2.conta = contas.ContaPoupanca(111, 1500, 0)
    # print(c2.nome)
    # print(c2.idade)

    banco = Banco()
    banco.cliente.extend([c1,c2])
    banco.conta.extend([c1.conta,c2.conta])
    banco.agencia.extend([111,222])
    print(banco)

    print(banco.autenticar(c1.conta, c2))
    print(banco.autenticar(c2.conta, c1))
    c1.conta.sacar(1)