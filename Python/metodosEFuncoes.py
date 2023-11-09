# Métodos e funções de listas

lista = [1, 3, 12, 8, 2]

# Métodos de inserção de elementos

# append - adiciona item ao final da lista (append = acrescentar)

print("Antes do append:", lista)

lista.append(3)

print("Depois do append:", lista)

# insert - adicionar item em posição especifica, indicado pelo índice

lista.insert(2, 10)

print("Depois do insert:", lista)

# extend - Utilizado para fazer a junção de 2 listas, adicionando os itens da segunda lista no final da primeira, semelhante ao append

lista2 = [1, 2, 3]

lista.extend(lista2)

print("Depois do extend:", lista)

# Métodos para remover elementos

# pop - remove o elemento de acordo com o índice informado ou o último elemento, caso não seja informado o índice desejado

lista.pop()

print("Lista apos o pop:", lista)

lista.pop(0)

print("Lista apos pop(0):", lista)

# remove - remove o primeiro elemento correspondente ao valor informado

lista.remove(3)

print("Lista apos o remove(3):", lista)

# count - conta a quantidade de vezes que um elemente se repete na lista

print("Quantidade do 2 na lista:", lista.count(2))

# index - Indica o índice do elemento informado

print("Índice do elemento 12:", lista.index(12))

# sort - Ordena a lista por padrão em ordem crescente, para ordem decrescente, inserir o argumento "reverse=True"

lista.sort()

print("Lista em ordem crescente:", lista)

lista.sort(reverse=True)
print("Lista em ordem decrescente:", lista)

#Funções para listas

# len - Retorna a quantidade de itens da lista

print("Quantidade de itens da lista",len(lista))

# sum - Soma todos os elementos da lista

print("Soma de todos os itens da lista:", sum(lista))

# max - Retorna o maior valor da lista

print("Maior valor da lista:", max(lista))

# min - Retorna o menor valor da lista

print("Menor valor da lista:", min(lista))