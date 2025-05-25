# Exercício 2.24: Dados de Primeira Classe (First-class Data)

No arquivo `portfolio.csv`, lemos dados organizados como colunas que se parecem com isto:

```csv
name,shares,price
"AA",100,32.20
"IBM",50,91.10
...
```

No código anterior, usamos o módulo `csv` para ler o arquivo, mas ainda tivemos que realizar conversões manuais de tipo. Por exemplo:

```python
for row in rows:
    name   = row[0]
    shares = int(row[1])
    price  = float(row[2])
```

Este tipo de conversão também pode ser realizado de uma maneira mais inteligente usando algumas operações básicas de lista.

Crie uma lista Python que contenha os nomes das funções de conversão que você usaria para converter cada coluna no tipo apropriado:

```python
>>> types = [str, int, float]
>>>
```

A razão pela qual você pode até criar esta lista é que tudo em Python é _first-class_ (de primeira classe). Então, se você quiser ter uma lista de funções, tudo bem. Os itens na lista que você criou são funções para converter um valor `x` em um determinado tipo (por exemplo, `str(x)`, `int(x)`, `float(x)`).

Agora, leia uma linha de dados do arquivo acima:

```python
>>> import csv
>>> f = open('portfolio.csv')
>>> rows = csv.reader(f)
>>> headers = next(rows)
>>> row = next(rows)
>>> row
['AA', '100', '32.20']
>>>
```

Como observado, esta linha não é suficiente para fazer cálculos porque os tipos estão errados. Por exemplo:

```python
>>> row[1] * row[2]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can't multiply sequence by non-int of type 'str'
>>>
```

No entanto, talvez os dados possam ser emparelhados com os tipos que você especificou em `types`. Por exemplo:

```python
>>> types[1]
<type 'int'>
>>> row[1]
'100'
>>>
```

Tente converter um dos valores:

```python
>>> types[1](row[1])     # Same as int(row[1])
100
>>>
```

Tente converter um valor diferente:

```python
>>> types[2](row[2])     # Same as float(row[2])
32.2
>>>
```

Tente o cálculo com valores convertidos:

```python
>>> types[1](row[1])*types[2](row[2])
3220.0000000000005
>>>
```

Zipe os tipos de coluna com os campos e veja o resultado:

```python
>>> r = list(zip(types, row))
>>> r
[(<type 'str'>, 'AA'), (<type 'int'>, '100'), (<type 'float'>,'32.20')]
>>>
```

Você notará que isso emparelhou uma conversão de tipo com um valor. Por exemplo, `int` é emparelhado com o valor `'100'`.

A lista zipada é útil se você quiser realizar conversões em todos os valores, um após o outro. Tente isto:

```python
>>> converted = []
>>> for func, val in zip(types, row):
          converted.append(func(val))
...
>>> converted
['AA', 100, 32.2]
>>> converted[1] * converted[2]
3220.0000000000005
>>>
```

Certifique-se de entender o que está acontecendo no código acima. No loop, a variável `func` é uma das funções de conversão de tipo (por exemplo, `str`, `int`, etc.) e a variável `val` é um dos valores como `'AA'`, `'100'`. A expressão `func(val)` está convertendo um valor (como um type cast).

O código acima pode ser compactado em uma única compreensão de lista.

```python
>>> converted = [func(val) for func, val in zip(types, row)]
>>> converted
['AA', 100, 32.2]
>>>
```
