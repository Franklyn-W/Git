Tipos de dados

Numéricos: representa números, que podem representar quantidade, volumes e realizar cálculos.

Existem dois tipos principais de números
* Inteiros: como o próprio nome diz, representa os números inteiros, sem casa decimal.
* Ponto flutuante: representam os números com casas decimais, engloba os numero reais

Texto: caracterizado por uma sequencia de caracteres, muitas vezes definidos entre aspas "" e que define uma palavra, uma expressão ou alguma coisa que será usada como um texto para exibição na tela ou processamento de leitura.

Boolean: possui apenas dois valores, verdadeiro ou falso. Muito utilizado para validações condicionais.

**O que é uma variável?**

Variável é um identificador de valor dentro da memoria, ele contem a informação do tipo do dado e o dado em si.

Pseudocódigo
```
INICIO principal
    VAR n1: INTEIRO
    VAR n2: INTEIRO
    VAR resultado: INTEIRO
    DEFINIR 0 -> n1
    DEFINIR 0 -> n2

    MOSTRAR "Digite o primeiro numero:
    ESPERAR_DIGITAÇÃO -> n1
    MOSTRAR "Digite o segundo numero:
    ESPERAR_DIGITAÇÃO -> n2
    SOMAR n1,n2 -> resultado
    MOSTRAR resultado
FIM
```

Teste de mesa

|comando|saída na tela|armazenamento
|--|--|--|
|DEFINIR 0 -> n1| |n1 = 0|
|DEFINIR 0 -> n2| |n1 = 0<br>n2 = 0|
|MOSTRAR "Digite o primeiro número:|"Digite o primeiro número:"|n1 = 0<br>n2 = 0|
|ESPERAR_DIGITAÇÃO -> n1| |n1 = 11<br>n2 = 0|
|MOSTRAR "Digite o segundo número:|"Digite o segundo número:"|n1 = 11<br>n2 = 0|
|ESPERAR_DIGITAÇÃO -> n2|  |n1 = 11<br>n2 = 31|
|SOMAR n1,n2 -> resultado| |n1 = 11<br>n2 = 31<br>resultado =42|
|MOSTRAR resultado|42|n1 = 11<br>n2 = 31<br>resultado =42|
|
