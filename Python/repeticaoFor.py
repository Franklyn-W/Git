# Laço de repetição For

# Estrutura de repetição para quando sabemos previamente a quantidade de vezes que o bloco de código será repetido, evitando repetições infinitas, como poder ocorrer com o While

for variável in range(10): 
    # vai repetir de 0 até o numero definido, exclusive
    print(variável)
print("----------------------")

for i in range(1,6):
    # vai repetir de 1 ate 5
    print(i)
print("----------------------")


for i in range(1,11,2):
    # vai repetir de 1 ate 10, pulando de 2 em 2
    print(i)

"""
Receber tres notas de uma aluno e fazer a media
"""
soma = 0

for i in range(1,4):
    nota = float(input(f"Informe a sua nota {i}: "))
    soma += nota

print(soma / 3)