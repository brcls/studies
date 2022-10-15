import re

endereco = "Rua das Flores 72, apartamento 1002, Laranjeiras, Rio de Janeiro, RJ, 23440-120"

# 5 dígitos + hífen (opcional) + 3 dígitos
# 99999-999
# 99999

padrao_cep = re.compile("[0-9]{5}[-]{0,1}[0-9]{3}")
busca = padrao_cep.search(endereco)

padrao_cep = "[0-9]{5}[-]{0,1}[0-9]{3}"
busca = re.search(padrao_cep, endereco)

if busca:
    cep = busca.group()
    print(cep)

else:
    print("CEP não encontrado")
