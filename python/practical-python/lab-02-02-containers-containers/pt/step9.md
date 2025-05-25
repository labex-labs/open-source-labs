# Exercício 2.4: Uma lista de tuplas (tuples)

O arquivo `portfolio.csv` contém uma lista de ações em uma carteira. No Exercício 1.30, você escreveu uma função `portfolio_cost(filename)` que lia este arquivo e realizava um cálculo simples.

Seu código deveria ter algo parecido com isto:

```python
# pcost.py

import csv

def portfolio_cost(filename):
    '''Computa o custo total (ações*preço) de um arquivo de carteira'''
    total_cost = 0.0

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            nshares = int(row[1])
            price = float(row[2])
            total_cost += nshares * price
    return total_cost
```

Usando este código como um guia aproximado, crie um novo arquivo `report.py`. Nesse arquivo, defina uma função `read_portfolio(filename)` que abre um determinado arquivo de carteira e o lê em uma lista de tuplas. Para fazer isso, você fará algumas pequenas modificações no código acima.

Primeiro, em vez de definir `total_cost = 0`, você criará uma variável que é inicialmente definida como uma lista vazia. Por exemplo:

```python
portfolio = []
```

Em seguida, em vez de totalizar o custo, você transformará cada linha em uma tupla exatamente como fez no último exercício e a anexará a esta lista. Por exemplo:

```python
for row in rows:
    holding = (row[0], int(row[1]), float(row[2]))
    portfolio.append(holding)
```

Finalmente, você retornará a lista `portfolio` resultante.

Experimente sua função interativamente (apenas um lembrete de que, para fazer isso, você primeiro precisa executar o programa `report.py` no interpretador):

_Dica: Use `-i` ao executar o arquivo no terminal_

```python
>>> portfolio = read_portfolio('/home/labex/project/portfolio.csv')
>>> portfolio
[('AA', 100, 32.2), ('IBM', 50, 91.1), ('CAT', 150, 83.44), ('MSFT', 200, 51.23),
    ('GE', 95, 40.37), ('MSFT', 50, 65.1), ('IBM', 100, 70.44)]
>>>
>>> portfolio[0]
('AA', 100, 32.2)
>>> portfolio[1]
('IBM', 50, 91.1)
>>> portfolio[1][1]
50
>>> total = 0.0
>>> for s in portfolio:
        total += s[1] * s[2]

>>> print(total)
44671.15
>>>
```

Esta lista de tuplas que você criou é muito semelhante a uma matriz 2-D. Por exemplo, você pode acessar uma coluna e linha específicas usando uma pesquisa como `portfolio[row][column]` onde `row` e `column` são inteiros.

Dito isso, você também pode reescrever o último loop for usando uma instrução como esta:

```python
>>> total = 0.0
>>> for name, shares, price in portfolio:
            total += shares*price

>>> print(total)
44671.15
>>>
```
