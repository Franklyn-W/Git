# Estrutura de listas

# Com as listas é possível realizar o armazenamento de varias informações dentro de uma única variável

# Antes
nota1 = 7.9
nota2 = 9.7
nota3 = 8.2

# Com lista

# Criando lista

notas = [7.9, 9.7, 8.2]

lista_vazia = []
lista = list()
lista = [26, "Franklyn", 3.14, False]
lista_de_listas = [20,[1,2,3], lista]

#Indexação e Slices(fatiamento)

# Indexação
print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])
# print(lista[4]) - IndexError: list index out of range

print(lista[-1]) # retorna o ultimo item da list
print(lista[-2]) # retorna o penúltimo item da list
# ...

# Slice

lista = [10, 50, 30, 40, 25, 60, 5]

print(lista[1:4]) # inicia no índice 1 e vai até o menor que 4
print(lista[3:]) # inicia no índice 3 e vai ate o final
print(lista[:5]) # percorre a lista até o índice menor que 5
print(lista[1:6:2]) # inicia no índice 1, vai ate o índice menor que 6, pulando de 2 em 2


# Iterações com laço FOR

# Utilizando os elementos da lista

for elemento in lista:
    print(elemento)

# Utilizando os indices

print("comprimento da lista: ", len(lista))

for i in range(len(lista)):
    print(lista[i])


