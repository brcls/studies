from abc import abstractmethod, ABCMeta
from operator import attrgetter
import array as arr
import numpy as np
from functools import total_ordering
# Lista -------------------------------------------------

idades = [39, 30, 27, 18, 15, 12, 9, 6, 3, 0]
len(idades)  # 10
idades[0]  # 39
idades.append(2)  # [39, 30, 27, 18, 15, 12, 9, 6, 3, 0, 2]
idades.remove(30)  # [39, 27, 18, 15, 12, 9, 6, 3, 0, 2]
idades.sort()  # [0, 2, 3, 6, 9, 12, 15, 18, 27, 39]
idades.reverse()  # [39, 27, 18, 15, 12, 9, 6, 3, 2, 0]
idades[0:3]  # [39, 27, 18]
idades[3:]  # [15, 12, 9, 6, 3, 2, 0]
idades[:3]  # [39, 27, 18]

18 in idades  # True

if 18 in idades:
    print('Sim, 18 está na lista')

idades.insert(0, 40)  # [40, 39, 27, 18, 15, 12, 9, 6, 3, 2, 0]
idades.extend([1, 2, 3])  # [40, 39, 27, 18, 15, 12, 9, 6, 3, 2, 0, 1, 2, 3]

idades_no_ano_que_vem = []
for idade in idades:
    idades_no_ano_que_vem.append(idade + 1)

idades_no_ano_que_vem = [idade + 1 for idade in idades]
idade_maior_que_18 = [idade for idade in idades if idade > 18]


def faz_processamento_de_visualizacao(lista=None):
    if lista is None:
        lista = list()
    # faz processamento de visualização
    print(len(lista))
    print(lista)
    lista.append(13)


class ContaCorrente:

    def __init__(self, codigo):
        self.saldo = 0.0
        self.codigo = codigo

    def deposita(self, valor):
        self.saldo += valor

    def __str__(self):
        return "[>>Codigo {} Saldo {}<<]".format(self.codigo, self.saldo)


conta_do_gui = ContaCorrente(15)
conta_do_gui.deposita(500)

conta_da_dani = ContaCorrente(47685)
conta_da_dani.deposita(1000)

contas = [conta_do_gui, conta_da_dani]
for conta in contas:
    print(conta)


def deposita_para_todas(contas):
    for conta in contas:
        conta.deposita(100)


deposita_para_todas(contas)

for conta in contas:
    print(conta)

# Tupla -------------------------------------------------

conta_do_gui = (15, 1000.0, 'Guilherme')


def deposita(conta):
    codigo = conta[0]
    novo_saldo = conta[1] + 100
    nome = conta[2]
    return (codigo, novo_saldo, nome)


conta_do_gui = deposita(conta_do_gui)
print(conta_do_gui)

guilherme = ('Guilherme', 37, 1981)
daniela = ('Daniela', 31, 1987)

usuarios = [guilherme, daniela]
usuarios.append(('Paulo', 39, 1979))

print(usuarios)


conta_do_gui = ContaCorrente(15)
conta_do_gui.deposita(500)

conta_da_dani = ContaCorrente(47685)
conta_da_dani.deposita(1000)

contas = (conta_do_gui, conta_da_dani)

for conta in contas:
    print(conta)

contas[0].deposita(300)

for conta in contas:
    print(conta)

# Herança e Polimorfismo -------------------------------------------------


class Conta(metaclass=ABCMeta):

    def __init__(self, codigo):
        self._saldo = 0.0
        self._codigo = codigo

    def deposita(self, valor):
        self._saldo += valor

    @abstractmethod
    def passa_o_mes(self):
        pass

    def __str__(self):
        return "[>>Codigo {} Saldo {}<<]".format(self._codigo, self._saldo)


class ContaCorrente(Conta):

    def passa_o_mes(self):
        self._saldo -= 2


class ContaPoupanca(Conta):

    def passa_o_mes(self):
        self._saldo *= 1.01
        self._saldo -= 3


class ContaInvestimento(Conta):

    def passa_o_mes(self):
        self._saldo *= 1.03


conta16 = ContaCorrente(16)
conta16.deposita(1000)
conta16.passa_o_mes()
print(conta16)

conta17 = ContaPoupanca(17)
conta17.deposita(1000)
conta17.passa_o_mes()
print(conta17)


contas = [conta16, conta17]  # Polimorfismo
for conta in contas:
    conta.passa_o_mes()
    print(conta)


# Array, não ter o costume de usar -------------------------------------------------

arr.array('d', [1, 3.5])  # array('d', [1.0, 3.5])
arr.array('i', [1, 2, 3, 4, 5, 6])  # array('i', [1, 2, 3, 4, 5, 6])


# Numpy -------------------------------------------------

numeros = np.array([1, 3.5])

numeros = numeros + 3
print(numeros)  # [4, 6.5]


# Igualdade -------------------------------------------------

class ContaSalario:

    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def deposita(self, valor):
        self._saldo += valor

    def __eq__(self, outro):
        if type(outro) != ContaSalario:
            return False
        return self._codigo == outro._codigo and self._saldo == outro._saldo

    def __str__(self):
        return "[>>Codigo {} Saldo {}<<]".format(self._codigo, self._saldo)


conta1 = ContaSalario(37)
conta2 = ContaSalario(37)

print(conta1 == conta2)  # True


# Outros builtins -------------------------------------------------

idades = [15, 87, 32, 65, 56, 32, 49, 37]

range(len(idades))  # range(0, 8)

for i in range(len(idades)):
    print(i, idades[i])

for i, idade in enumerate(idades):
    print(i, idade)

ususarios = [
    ("Guilherme", 37, 1981),
    ("Daniela", 31, 1987),
    ("Paulo", 39, 1979),
]

for nome, idade, nascimento in ususarios:  # unpacking
    print(nome)

for nome, _, _ in ususarios:  # unpacking
    print(nome)

# Sorted e Sort -------------------------------------------------

idades = [15, 87, 32, 65, 56, 32, 49, 37]

print(idades)
print(sorted(idades))
print(list(reversed(idades)))
print(sorted(idades, reverse=True))

idades.sort()
print(idades)

idades.sort(reverse=True)
print(idades)

nomes = ['Guilherme', 'Daniela', 'Paulo']

print(nomes)
print(sorted(nomes))


@total_ordering
class ContaSalario:

    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def deposita(self, valor):
        self._saldo += valor

    def __eq__(self, outro):
        if type(outro) != ContaSalario:
            return False
        return self._codigo == outro._codigo and self._saldo == outro._saldo

    def __lt__(self, outro):
        if self._saldo != outro._saldo:
            return self._saldo < outro._saldo
        return self._codigo < outro._codigo

    def __str__(self):
        return "[>>Codigo {} Saldo {}<<]".format(self._codigo, self._saldo)


conta_do_guilherme = ContaSalario(37)
conta_da_daniela = ContaSalario(31)
conta_do_paulo = ContaSalario(39)

conta_do_guilherme.deposita(500)
conta_da_daniela.deposita(1000)
conta_do_paulo.deposita(510)

contas = [conta_do_guilherme, conta_da_daniela, conta_do_paulo]

for conta in sorted(contas, key=attrgetter('_saldo')):
    print(conta)

for conta in sorted(contas, key=lambda conta: conta._saldo):
    print(conta)

for conta in sorted(contas):  # ordenação natural
    print(conta)

for conta in sorted(contas, reverse=True):  # ordenação natural
    print(conta)

# Ordenação total -------------------------------------------------

for conta in sorted(contas, key=attrgetter('_saldo', '_codigo')):
    print(conta)

print(conta_do_guilherme <= conta_da_daniela)  # True
