# Definindo Funções

É uma boa ideia colocar todo o código relacionado a uma única _tarefa_ em um só lugar. Use uma função.

```python
def read_prices(filename):
    prices = {}
    with open(filename) as f:
        f_csv = csv.reader(f)
        for row in f_csv:
            prices[row[0]] = float(row[1])
    return prices
```

Uma função também simplifica operações repetidas.

```python
oldprices = read_prices('oldprices.csv')
newprices = read_prices('newprices.csv')
```
