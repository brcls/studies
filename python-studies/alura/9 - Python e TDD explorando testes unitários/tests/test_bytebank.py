from codigo.bytebank import Funcionario
import pytest
from pytest import mark


class TestClass:
    def test_quando_idade_recebe_13_03_2000_deve_retornar_22(self):
        entrada = '13/03/2000'  # Given-contexto
        esperado = 22  # When-contexto

        funcionario_teste = Funcionario('Teste', entrada, 1000)
        resultado = funcionario_teste.idade()  # When-ação

        assert resultado == esperado  # Then-desfecho

    def test_quando_sobrenome_recebe_lucas_carvalho_deve_retornar_carvalho(self):
        entrada = 'Lucas Carvalho'
        esperado = 'Carvalho'

        funcionario_teste = Funcionario(entrada, '13/03/1990', 1000)
        resultado = funcionario_teste.sobrenome()

        assert resultado == esperado

    def test_quando_decrescimo_salario_recebe_100000_deve_retornar_90000(self):
        entrada_salario = 100000  # Given-contexto
        entrada_nome = "Paulo Bragança"
        esperado = 90000

        funcionario_teste = Funcionario(
            entrada_nome, '13/03/1990', entrada_salario)
        funcionario_teste.decrescimo_salario()

        resultado = funcionario_teste.salario

        assert resultado == esperado

    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_1000_deve_retornar_100(self):
        entrada_salario = 1000
        entrada_nome = "Paulo Bragança"
        esperado = 100

        funcionario_teste = Funcionario(
            entrada_nome, '13/03/1990', entrada_salario)
        resultado = funcionario_teste.calcular_bonus()

        assert resultado == esperado

    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_100000_deve_retornar_exception(self):
        with pytest.raises(Exception):
            entrada_salario = 100000
            entrada_nome = "Paulo Bragança"

            funcionario_teste = Funcionario(
                entrada_nome, '13/03/1990', entrada_salario)
            funcionario_teste.calcular_bonus()
