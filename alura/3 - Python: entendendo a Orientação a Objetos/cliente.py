class Cliente:

    def __init__(self, nome):
        self.nome = nome

    @property
    def nome(self):
        return self.nome.title()

    @nome.setter
    def nome(self, nome):
        self.nome = nome
