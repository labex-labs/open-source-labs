# Exercício 1.33: Lendo da linha de comando

No programa `pcost.py`, o nome do arquivo de entrada foi codificado no código:

```python
# pcost.py

def portfolio_cost(filename):
    ...
    # Your code here
    ...

cost = portfolio_cost('portfolio.csv')
print('Total cost:', cost)
```

Isso é bom para aprendizado e testes, mas em um programa real você provavelmente não faria isso.

Em vez disso, você pode passar o nome do arquivo como um argumento para um script. Tente alterar a parte inferior do programa da seguinte forma:

```python
# pcost_1.33.py

import csv


def portfolio_cost(filename):
    """
    Computes the total cost (shares*price) of a portfolio file
    """
    total_cost = 0.0

    with open(filename, "rt") as f:
        rows = csv.reader(f)
        headers = next(rows)  # Skip header row
        for row in rows:
            if len(row) < 3:
                print("Skipping invalid row:", row)
                continue
            try:
                nshares = int(row[1])
                price = float(row[2])
                total_cost += nshares * price
            except (IndexError, ValueError):
                print("Skipping invalid row:", row)

    return total_cost

import sys


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'portfolio.csv'

cost = portfolio_cost(filename)
print('Total cost:', cost)
```

`sys.argv` é uma lista que contém os argumentos passados na linha de comando (se houver).

Para executar seu programa, você precisará executar o Python a partir do terminal.

Por exemplo, no bash no Unix:

```bash
$ python3 pcost.py portfolio.csv
Total cost: 44671.15
bash %
```
