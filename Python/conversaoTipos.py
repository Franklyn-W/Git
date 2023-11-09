# Conversão de tipos

idade = "30"
print(idade, type(idade))


idade_inteira = int(idade)
print(idade_inteira, type(idade_inteira))

"""
    int()
    str()
    float()
    bool()
"""

altura = input("Informe sua altura: ")
# Por padrão, o input recebe as entradas como str, sendo necessário especificar, caso deseja o armazenamento dos dados com outro tipo
print(altura, type(altura))

altura2 = float(input("Informe sua altura: "))
print(altura2, type(altura2))