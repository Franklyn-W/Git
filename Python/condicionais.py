# Estruturas condicionais

idade = 18

if idade >= 18:
    print("Maior de idade")
else:
    print("Menor de idade")

"""
Mostrar "Aprovado", caso a média seja maior ou igual a 7, e "Reprovado", caso a média seja menor que 7
"""

media = float(input("Informe a nota média do aluno: "))

if media >= 7:
    print("Aprovado")
elif media >= 5:
    print("Recuperação")
else:
    print("Reprovado")


presença = 80

if media >= 7 and presença >= 70:
    print("Aprovado")
else:
    print("Reprovado")
