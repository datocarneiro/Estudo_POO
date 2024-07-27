# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados.
import json

class Pessoa:
    def __init__(self, nome , idade):
        self.nome = nome 
        self.idade = idade

p1 = Pessoa('Dato', 20)

print(vars(p1).json)
#resultado:     {'nome': 'Dato', 'idade': 20}