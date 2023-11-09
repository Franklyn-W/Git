# Laço de repetição While (enquanto)

# Laço de repetição utilizado para repetir a execução de sequencia de código, caso alguma condição pre-estabelecida seja verdadeira

numero_aleatório = 15

numero_escolhido = int(input("Informe um numero entre 1 e 20: "))

while numero_escolhido != numero_aleatório:
    print("Erroooou!!! Tente novamente")
    numero_escolhido = int(input("Informe um numero entre 1 e 20: "))
print("Você acertou!!!")


# Usando variável como contador

contador = 0

while contador <5:
    print(contador)
    
    contador += 1