# 1. Variáveis
# Python possui tipagem dinâmica, não necessitando informar o tipo do dado a ser atribuído a variável

idade = 26 
# Criação de variável idade, recebendo valor 26

print(idade)

nome = "Franklyn Winston"
# Variável nome recebendo texto

print(nome)

"""
    Tipo de variáveis

    1. int = números inteiros, ou seja, números sem parte decimal: 0, 5, -1, 1000
    2. float = números reais, ou seja, números com a parte decimal: 1.0, -2.7, 3.14
    3. string = cadeia de carácteres, ou seja, dados textuais
    4. bool = valores lógicos (booleanos): True ou False
"""

idade = 26
nome = "Franklyn"
altura = 1.75
estudando = True

print(type(idade))
print(type(nome))
print(type(altura))
print(type(estudando))

# Armazenando dados inseridos pelo usuário

linguagem = input("Qual a linguagem esta estudando agora? ")
print("A linguagem que você esta estudando é: ", linguagem)

# inserindo mais de uma variável dentro de um print
print("Idade: ", idade, ", Nome: ", nome, ", Altura: ", altura, " Esta estudando? ", estudando, ", Qual linguagem: ", linguagem)