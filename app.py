class contaCliente():
    def __init__(self, nome, saldo):
        self.nome = nome
        self.saldo = saldo

    def menu():
        escolha = 0
        while (escolha != 4):
            print('Escolha uma opção:')
            print('\t1 - Consultar Saldo:')
            print('\t2 - Realizar depósito:')
            print('\t3 - Realixar saque:')
            print('\t4 - Sair:')
            escolha = int(input())

            if not isinstance(escolha, int):
                return "opção inválida"
            elif(escolha == 1): 
                return contaCliente.consultarSaldo()
            else:
                return 'else'



        print('saiu do while')
        return f'return...', escolha   
    
    def consultarSaldo():
        return 'chegou return saldo'
    
cliente1 = (input('Digite nome: '))
contaCliente(cliente1, saldo = 0)
contaCliente.menu()