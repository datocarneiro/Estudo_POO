class ContaCliente:
    def __init__(self, nome, saldo=0):
        self.nome = nome
        self.saldo = saldo

    def menu(self):
        modulos = ['Consultar Saldo', 'Realizar depósito', 'Realizar Saque', 'Sair']
        print(f'='*50)  
        print(f'Cliente: {self.nome}, escolha um módulo:')
        for i, modulo in enumerate(modulos):
            print(f'\t[{i+1}] - {modulo}')

    def main(self,modulo=0):
        while modulo !=4:
            ContaCliente.menu(self)
            try:
                print()
                modulo = int(input('Modulo: '))
                print(f'='*50)  
                if modulo < 1 or modulo > 4:
                    print('Escola diferente')
                if modulo == 1: 
                    print(self.getSaldo())
                if modulo == 2: 
                    print(self.realizarDeposito())
                if modulo == 3: 
                    print(self.realizarSaque())
            except ValueError:
                print('|OPÇÃO INVALIDA...digite um numero')
        return '\t\t\t\t\t\t|| ...Saindo do menu'


    def getSaldo(self):
        return f'{self.nome}, seu saldo atual é: R$ {self.saldo}'
    
    def realizarDeposito(self):
        deposito = float(input('Valor de depósito: '))
        self.saldo += deposito
        return f'Valor {deposito} depositado com sucesso'
    
    def realizarSaque(self):
        saque = float(input('Valor de Saque: '))
        self.saldo -= saque
        return f'Valor {saque} sacado com sucesso'

cliente1 = ContaCliente('Joshua')
print(ContaCliente.main(cliente1))

cliente2 = ContaCliente('Mathias')
print(ContaCliente.main(cliente2))
