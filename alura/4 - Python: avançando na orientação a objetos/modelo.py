class Filme:
    def __init__(self, nome, ano, duracao):
        self.__nome = nome.title()
        self.ano = ano
        self.duracao = duracao
        self.__likes = 0

    @property
    def likes(self):
        return self.__likes

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome.title()

    def dar_likes(self):
        self.likes += 1

    def __str__(self):
        return f'Nome {self.__nome}, ano {self.ano}, duração {self.duracao} - Likes {self.__likes}'


class Serie:
    def __init__(self, nome, ano, temporadas):
        self.nome = nome.title()
        self.ano = ano
        self.temporadas = temporadas
        self.likes = 0

    @property
    def likes(self):
        return self.__likes

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome.title()

    def dar_likes(self):
        self.likes += 1

    def __str__(self):
        return f'Nome: {self.nome} ({self.ano}) - {self.temporadas} temporadas - Likes: {self.likes}'


vingadores = Filme('vingadores - guerra infinita', 2018, 160)
print(vingadores)

atlanta = Serie('atlanta', 2018, 2)
print(atlanta)
