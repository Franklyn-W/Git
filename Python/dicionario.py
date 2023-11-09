# Dicionários

# Dicionário é uma especie de lista que utiliza chave e valor para cada elemento

# Criando um dicionário

# Criando dicionario vazio
dicionario = {}
dicionario = dict()

# Criando dicionario com valores

dicionario = {"nome": "Franklyn", "idade": 30, "altura": 1.75}

print(dicionario)
print(dicionario["idade"])


# Adicionando elementos

dicionario["programador"] = True # Adiciona a chave inexistente e seu valor
print(dicionario)

dicionario["altura"] = 2 # Substitui o valor da chave 'idade'
print(dicionario)


# Iterando sobre um dicionário

for chave in dicionario:
    print(chave, dicionario[chave])


# Verificando existência de uma chave

print("peso" in dicionario) # Verificando se a chave 'peso' existe no dicionario
print("altura" in dicionario)