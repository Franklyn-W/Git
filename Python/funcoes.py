# Funções

# 1 O que é e porque utilizar funções? 

# Funções já utilizadas

"""
print() - imprime conteúdo na tela
input() - recebe um dado do usuário
len() - retorna o tamanho de uma lista
max() - Retorna o maior valor de uma lista
"""

# 2 Criação de uma função

# Função inicial

def saudacao():
    print("Seja bem vindo(a)")
    print("Olá, é um prazer te ver aqui!")

saudacao()

# Função com parâmetros

def saudacao2(nome, curso):
    print(f"Seja bem vindo(a) {nome}")
    print(f"Olá, é um prazer te ver aqui no curso de {curso}!")

saudacao2("Franklyn", "Python")
saudacao2("Carolina", "Javascript")

# Funções com parâmetros default

def saudacao3(nome, curso = "Java"):
    print(f"Seja bem vindo(a) {nome}")
    print(f"Olá, é um prazer te ver aqui no curso de {curso}!")

saudacao3("Franklyn")

# Funções com retorno

def soma(num1, num2):
    return num1 + num2
    O_que_estiver_apos_o_return_sera_ignorado

resultado = soma(5, 7)

print("O resultado da soma é:", resultado)

def calculadora(num1, num2, operacao = "+"):
    if operacao == "+":
        return num1 + num2
    elif operacao == "-":
        return num1 - num2

resultado = calculadora(10,20)
print(resultado)

resultado = calculadora(10,20,"-")
print(resultado)


