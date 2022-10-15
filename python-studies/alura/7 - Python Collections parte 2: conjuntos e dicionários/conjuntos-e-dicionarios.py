from collections import defaultdict, Counter
from typing import Counter

# Conjuntos

conjunto = set([1, 2])

usuarios_data_science = {15, 23, 43, 56}
usuarios_machine_learning = {15, 23, 105, 9}

assistiram = usuarios_data_science | usuarios_machine_learning
assistiram_os_dois_cursos = usuarios_data_science & usuarios_machine_learning
assistiram_so_data_science = usuarios_data_science - usuarios_machine_learning
assistiram_so_um_dos_cursos = usuarios_data_science ^ usuarios_machine_learning

for usuario in assistiram:
    print("Assistiram", usuario)

for usuario in assistiram_os_dois_cursos:
    print("Assistiram os dois", usuario)

for usuario in assistiram_so_data_science:
    print("Assistiram só Data Science", usuario)

for usuario in assistiram_so_um_dos_cursos:
    print("Assistiram só um dos cursos", usuario)

usuarios = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
usuarios.add(11)
usuarios.remove(1)
usuarios = frozenset(usuarios)
print(usuarios)

meu_texto = "Bem vindo meu nome é Guilherme e meu nome é Guilherme"
meu_texto = meu_texto.split()
meu_texto = set(meu_texto)

print(meu_texto)

# Dicionários

aparaicoes = dict(Guilherme=1, João=2, Maria=1)
aparicoes = {"Guilherme": 1, "João": 2, "Maria": 1}
print(aparicoes["Guilherme"])
print(aparicoes.get("Guilherme", 0))

aparicoes["Guilherme"] = 2
aparicoes["Carlos"] = 1
del aparicoes["Guilherme"]

print("Carlos" in aparicoes)

for elemento in aparicoes:
    print(elemento)

for elemento in aparicoes.keys():
    print(elemento)

for elemento in aparicoes.values():
    print(elemento)

for elemento in aparicoes.items():
    print(elemento)

for chave, valor in aparicoes.items():
    print(chave, valor)

print(["Palavra - {}".format(chave) for chave in aparicoes.keys()])

meu_texto = "Bem vindo meu nome é Guilherme e meu nome é Guilherme"
meu_texto = meu_texto.lower()

aparicoes_de_palavra = {}

for palavra in meu_texto.split():
    aparicoes_de_palavra[palavra] = aparicoes_de_palavra.get(palavra, 0) + 1

# -------------

aparaicoes_de_palavra = defaultdict(int)

for palavra in meu_texto.split():
    aparicoes_de_palavra[palavra] += 1

print(meu_texto)
print(aparicoes_de_palavra)


class Conta:
    def __init__(self):
        print("Criando conta ...")


contas = defaultdict(Conta)
contas[15]
contas[88]

meu_texto = "Bem vindo meu nome é Guilherme e meu nome é Guilherme"
meu_texto = meu_texto.lower()

aparicoes_de_palavra = Counter(meu_texto.split())

# Testando o uso de diversas coleções

texto1 = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer ac libero ut lorem laoreet sollicitudin. Nulla rutrum aliquam gravida. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Sed vitae dolor lectus. Cras quis aliquet nisl. Nam tincidunt magna vitae pretium sagittis. Quisque condimentum auctor ligula id accumsan. Mauris consectetur feugiat turpis, at efficitur diam varius nec. Quisque iaculis tempor facilisis. Duis a metus sed ipsum semper sodales at vitae mi. Sed ullamcorper, sem quis malesuada tempor, justo nulla rutrum enim, vel accumsan nisi orci a dolor. Nulla bibendum, sapien id iaculis consequat, diam erat condimentum purus, et interdum massa lectus faucibus augue. Etiam eu lectus sit amet augue congue sodales. Pellentesque non libero purus. Vestibulum scelerisque sapien sit amet enim tempor varius.
"""
texto2 = """
Praesent blandit eros vehicula, viverra magna blandit, bibendum purus. Nam consequat ornare varius. Nulla porttitor pulvinar suscipit. Vivamus ipsum arcu, facilisis quis dolor eget, elementum rutrum eros. Etiam tincidunt tortor velit. Morbi in mi vitae lectus viverra dapibus ut vel elit. Duis non metus quam. Quisque in neque gravida, molestie ex ut, tempus felis. Nunc accumsan rhoncus libero et sollicitudin. Aliquam at ante ac elit rutrum tristique vel nec ante. Phasellus rhoncus metus et mi semper, quis egestas ligula porttitor. Donec eget luctus ex, nec fringilla quam. Integer congue justo ac tristique consequat.
"""

aparicoes_de_palavra = Counter(texto1.split())
print(aparicoes_de_palavra)

aparicoes_de_letra = Counter(texto1.lower())
print(aparicoes_de_letra)

total_de_letras = sum(aparicoes_de_letra.values())
print(total_de_letras)

probabilidade_de_letra = {
    letra: aparicoes / total_de_letras
    for letra, aparicoes in aparicoes_de_letra.items()
}

mais_comuns = Counter(probabilidade_de_letra).most_common(10)

for caractere, probabilidade in mais_comuns:
    print("{} - {:.2f}%".format(caractere, probabilidade * 100))
