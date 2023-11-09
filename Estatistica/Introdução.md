# Conteúdo de estatística

* Introdução à estatística e amostragem
* Tipo de dados, tabelas e distribuição de frequência
* Visualização gráfica
* Medidas de posição e medidas de dispersão (variabilidade)
* Análise bidimensional
* Regressão Linear Simples
* Introdução à probabilidade
* Probabilidade
* Analise Combinatória
* Probabilidade total, parcial e teorema de Bayes

### Introdução

A estatística é a ciência que estuda os métodos de coleta, análise, organização, descrição, interpretação e apresentação de dados experimentais. Os dados são obtidos com o intuito de responder um problema do mundo real

A estatística subdivide-se em três grandes áreas:
* A estatística descritiva: Parte da estatística voltada para a organização e descrição do dados;
* Probabilidade: Útil para avaliar situações em que envolvem o acaso;
* Inferência: Refere-se à análise e interpretação do dados

### Amostragem

Amostra é todo subconjunto de unidade retiradas de uma população. O processo de retirada de informações dos 'n' elementos amostrais, deve seguir um método criterioso e adequado que são os tipos de amostragem.

Basicamente existem amostrar probabilísticas e não probabilísticas:

* Amostra probabilística: todos os elementos da população apresentam probabilidade maior que zero de serem selecionados(aleatória simples, estratificada, sistemática e por conglomerados).
* Amostra não probabilística: quando não há probabilidade clara/conhecida de seleção dos elementos. Os elementos são escolhidos de forma julgamental(acidental, intencional, por cotas).

### Técnicas de amostragem probabilísticas

* **Amostra Aleatória Simples (AAS)**

A amostra aleatória simples pode ser realizada com ou sem reposição. No caso em que há reposição, cada elementos pode ser sorteado mais de uma vez. Para exemplificar, suponha que se queira sortear um número aleatório de uma urna, se for uma Amostra Aleatória Simples (AAS) com reposição, este número voltará para urna para participar do próximo sorteio. Se não houver reposição, cada elemento só poderá ser selecionado uma vez para compor a amostra.

* **Amostra Estratificada**

Neste tipo de amostragem, a população é dividida em estrato homogêneos (grupos com elementos de características comuns) e é selecionada uma amostra aleatória de cada estrato.

*Exemplo*  
Numa sala existem 90 alunos, sendo 54 do sexo masculino e 36 do sexo feminino e queremos uma amostra de 10% da população e que respeite a proporção entre meninos e meninas.

| Sexo  | População | 10% | Amostra |
| ----- | --------- | --- | ------- |
| M     | 54        | 5,4 | 5       |
| F     | 36        | 3,6 | 4       |
| Total | 90        | 9   | 9       |

* **Amostra Sistemática**

Os elementos são selecionados seguindo uma regra pré-definida.

*Exemplo*  
Uma rua possui 900 casas e queremos formar uma amostra composta por 50 casas. Para isso vamos construir uma regra de amostragem.  
Primeiro vamos dividir o total de casas pelo tamanho da amostragem  

```
900 / 50 = 18
```

Selecionamos as 18 primeiras casas e realizamos o primeiro sorteio entre eles. Para a demais casas, somaremos 18 ao numero da casa anterior, assim teremos a seguinte distribuição
```
Primeira casa sorteada: 04
Somando 18, teremos o numero da proxima casa, que é a casa 22.

Lista de casas sorteadas: 04, 22, 40, 58, 76 ...
```


* **Amostra por conglomerado**

Neste tipo de amostragem aleatória, a população (extensa) é dividida em miniaturas da população (não homogêneas) e seleciona-se uma amostra aleatória desses conglomerados.

*Exemplo*  

Podemos tomar como exemplo a distribuição de um estado, que pode ser dividido em cidades, bairros, quarteirões, ruas, casas, famílias, entre outras divisões.

*Exemplo2*

O objetivo de uma pesquisa é determinar a renda familiar dos moradores de uma cidade. Para realizar essa analise podemos utilizar os setores censitários do IBGE, que divide uma cidade em "bairro" e selecionar um setor e utiliza-lo como amostra dessa cidade.

### Conclusão

A estatística é a coleção dee métodos para planejar experimentos, obter e organizar dados, resumi-los, analisá-los, interpretá-los e deles extrair conclusões. A estatística descritiva trata da organização, resumo e apresentação dos dados, a probabilidade trata dos eventos aleatórios e a estatística inferencial, busca, a partir de uma amostra, obter conclusões sobre a população.

A obtenção de uma amostra é o processo de amostragem, que pode ser um processo probabilístico ou não probabilístico.

Este conteúdo apresentou as abordagens de amostragem probabilísticas, mas há também abordagens não-probabilísticas, que são alternativas em alguns casos específicos.