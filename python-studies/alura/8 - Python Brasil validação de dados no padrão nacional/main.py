from cpf_cnpj import Documento
from TelefonesBr import TelefonesBr
from datas_br import DatasBr
from acesso_cep import BuscaEndereco

cpf = '35442641022'
print("\nCru ->", cpf, "\nFormatado ->", Documento.criar_novo(cpf))

cnpj = '27912997000102'
print("\nCru ->", cnpj, "\nFormatado ->", Documento.criar_novo(cnpj))

telefone = '5511999999999'
print("\nCru ->", telefone, "\nFormatado ->", TelefonesBr(telefone))

cadastro = DatasBr()
print("\nData de cadastro ->", cadastro.momento_cadastro)
print("Mes de cadastro ->", cadastro.mes_cadastro())
print("Dia da semana ->", cadastro.dia_semana())
print("Data formatada ->", cadastro)
print("Tempo de cadastro ->", cadastro.tempo_cadastro())

cep = '01001000'
objeto_cep = BuscaEndereco(cep)
print("\nCEP ->", objeto_cep)
print("Bairro ->", objeto_cep.acessa_via_cep()[0])
print("Cidade ->", objeto_cep.acessa_via_cep()[1])
print("Estado ->", objeto_cep.acessa_via_cep()[2])
