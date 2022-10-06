url = "https://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100"
print("url ->", url)

# Sanitização da url
url = url.strip()

# Valida a URL
if url == "":
    raise ValueError("A URL está vazia")

# Separa base e os parâmetros
indice_interrogacao = url.find("?")

url_base = url[:indice_interrogacao]
print("url base ->", url_base)

url_parametros = url[indice_interrogacao+1:]
print("parametro ->", url_parametros)

# Busca o valor de um parâmetro
parametro_busca = "quantidade"
indice_parametro = url_parametros.find(parametro_busca)
print("indice parametro ->", indice_parametro)

indice_valor = indice_parametro + len(parametro_busca) + 1
indice_e_comercial = url_parametros.find("&", indice_valor)

if indice_e_comercial == -1:
    valor = url_parametros[indice_valor:]
else:
    valor = url_parametros[indice_valor:indice_e_comercial]

print("valor ->", valor)
