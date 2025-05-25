# Por que dicionários? (Why dictionaries?)

Dicionários são úteis quando há _muitos_ valores diferentes e esses valores podem ser modificados ou manipulados. Dicionários tornam seu código mais legível.

```python
s['price']
# vs
s[2]
```

Nos últimos exercícios, você escreveu um programa que lia um arquivo de dados `portfolio.csv`. Usando o módulo `csv`, é fácil ler o arquivo linha por linha.

```python
>>> import csv
>>> f = open('portfolio.csv')
>>> rows = csv.reader(f)
>>> next(rows)
['name', 'shares', 'price']
>>> row = next(rows)
>>> row
['AA', '100', '32.20']
>>>
```

Embora a leitura do arquivo seja fácil, você geralmente quer fazer mais com os dados do que apenas lê-los. Por exemplo, talvez você queira armazená-los e começar a realizar alguns cálculos neles. Infelizmente, uma "linha" bruta de dados não fornece o suficiente para trabalhar. Por exemplo, mesmo um cálculo matemático simples não funciona:

```python
>>> row = ['AA', '100', '32.20']
>>> cost = row[1] * row[2]
Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
TypeError: can't multiply sequence by non-int of type 'str'
>>>
```

Para fazer mais, você normalmente quer interpretar os dados brutos de alguma forma e transformá-los em um tipo de objeto mais útil para que possa trabalhar com ele mais tarde. Duas opções simples são tuplas ou dicionários.
