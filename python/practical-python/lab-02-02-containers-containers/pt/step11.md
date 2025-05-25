# Exercício 2.6: Dicionários (Dictionaries) como um contêiner (container)

Um dicionário é uma maneira útil de acompanhar itens onde você deseja procurar itens usando um índice diferente de um inteiro. No shell do Python, tente brincar com um dicionário:

```python
>>> prices = { }
>>> prices['IBM'] = 92.45
>>> prices['MSFT'] = 45.12
>>> prices
... veja o resultado ...
>>> prices['IBM']
92.45
>>> prices['AAPL']
... veja o resultado ...
>>> 'AAPL' in prices
False
>>>
```

O arquivo `prices.csv` contém uma série de linhas com preços de ações. O arquivo se parece com isto:

```csv
"AA",9.22
"AXP",24.85
"BA",44.85
"BAC",11.27
"C",3.72
...
```

Escreva uma função `read_prices(filename)` que lê um conjunto de preços como este em um dicionário onde as chaves do dicionário são os nomes das ações e os valores no dicionário são os preços das ações.

Para fazer isso, comece com um dicionário vazio e comece a inserir valores nele, assim como você fez acima. No entanto, você está lendo os valores de um arquivo agora.

Usaremos esta estrutura de dados para procurar rapidamente o preço de um determinado nome de ação.

Algumas pequenas dicas que você precisará para esta parte. Primeiro, certifique-se de usar o módulo `csv` como você fez antes --- não há necessidade de reinventar a roda aqui.

```python
>>> import csv
>>> f = open('/home/labex/project/prices.csv', 'r')
>>> rows = csv.reader(f)
>>> for row in rows:
        print(row)


['AA', '9.22']
['AXP', '24.85']
...
[]
>>>
```

A outra pequena complicação é que o arquivo `prices.csv` pode ter algumas linhas em branco nele. Observe como a última linha de dados acima é uma lista vazia --- significando que nenhum dado estava presente nessa linha.

Existe a possibilidade de que isso possa fazer com que seu programa morra com uma exceção. Use as instruções `try` e `except` para capturar isso conforme apropriado. Pensamento: seria melhor proteger contra dados ruins com uma instrução `if` em vez disso?

Depois de escrever sua função `read_prices()`, teste-a interativamente para garantir que funcione:

```python
>>> prices = read_prices('/home/labex/project/prices.csv')
>>> prices['IBM']
106.28
>>> prices['MSFT']
20.89
>>>
```
