Fluxo de processamento de algoritmo

Inicio > Entrada > Processamento > Saida > Final

Exemplo

Inicio > "Nome da pessoa" > Processamento > "Bom dia, "Nome da pessoa" > Final

Abstraindo processo

Inicio
    Pedir nome da pessoa
        Armazenar o nome da pessoa
            Juntar o nome ao texto de "Bom dia"
                Mostrar a frase montada
                    Final

Passo a passo

INICIO principal 
    MOSTRAR "Digite seu nome: "
    ESPERAR_DIGITAÇÃO -> nome
    JUNTAR_TEXTO "Bom dia" + nome -> saudação
    MOSTRAR_TEXTO saudação
FIM

tabela de teste de uso  
|Comando|Saida na tela|Armazenamento|
|--|--|--|
|MOSTRAR "Digite seu nome: "|"Digite seu nome"|--|
|ESPERAR_DIGITAÇÃO -> nome|--|Nome = "Jose"|
|JUNTAR_TEXTO "Bom dia" + nome -> saudação|--|Nome = "Jose"<br>saudação = "Bom dia Jose"|
|MOSTRAR_TEXTO saudação|**Bom dia Jose**|Nome = "Jose"<br>saudação = "Bom dia Jose"|
|

