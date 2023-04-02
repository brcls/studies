class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def registra_horas(self, horas):
        print('Horas registradas...')

    def mostra_tarefas(self):
        print('Fez muita coisa...')


class Caelum(Funcionario):
    def mostra_tarefas(self):
        print('Fez muita coisa, Caelumer!')

    def busca_cursos_do_mes(self, mes=None):
        print(f'Mostrando cursos - {mes}')


class Alura(Funcionario):
    def mostra_tarefas(self):
        print('Fez muita coisa, Alurete!')

    def busca_perguntas_sem_resposta(self):
        print('Mostrando perguntas não respondidas do fórum')


class Hipster:
    def __str__(self):
        return f'Hipster, {self.nome}'

    def __len__(self):
        return 42


class Junior(Alura):
    pass


class Pleno(Alura, Caelum):
    pass


class Senior(Alura, Caelum, Hipster):
    pass


luan = Senior("Luan", 3000)
print(luan)
