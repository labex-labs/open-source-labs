# Exercício 1.30: Transformando um script em uma função

Pegue o código que você escreveu para o programa `pcost.py` no Exercício 1.27 e transforme-o em uma função `portfolio_cost(filename)`. Esta função recebe um nome de arquivo como entrada, lê os dados do portfólio nesse arquivo e retorna o custo total do portfólio como um float.

Para usar sua função, altere seu programa para que ele se pareça com isto:

```python
# pcost.py
def portfolio_cost(filename):
    """
    Computes the total cost (shares*price) of a portfolio file
    """
    total_cost = 0.0

    with open(filename, "rt") as f:
        rows = f.readlines()
        headers = rows[0].strip().split(",")
        for row in rows[1:]:
            row_data = row.strip().split(",")
            nshares = int(row_data[1])
            price = float(row_data[2])
            total_cost += nshares * price

    return total_cost


import sys

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = input("Enter a filename:")

cost = portfolio_cost(filename)
print("Total cost:", cost)
```

Quando você executar seu programa, deverá ver a mesma saída de antes. Depois de executar seu programa, você também pode chamar sua função interativamente digitando isto:

```bash
$ python3 -i pcost.py
```

Isso permitirá que você chame sua função do modo interativo.

```python
>>> portfolio_cost('portfolio.csv')
44671.15
>>>
```

Poder experimentar seu código interativamente é útil para testes e depuração.
