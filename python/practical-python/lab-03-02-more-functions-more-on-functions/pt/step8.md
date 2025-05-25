# Variáveis Locais (Local Variables)

Variáveis atribuídas dentro de funções são privadas.

```python
def read_portfolio(filename):
    portfolio = []
    for line in open(filename):
        fields = line.split(',')
        s = (fields[0], int(fields[1]), float(fields[2]))
        portfolio.append(s)
    return portfolio
```

Neste exemplo, `filename`, `portfolio`, `line`, `fields` e `s` são variáveis locais. Essas variáveis não são retidas ou acessíveis após a chamada da função.

```python
>>> stocks = read_portfolio('portfolio.csv')
>>> fields
Traceback (most recent call last):
File "<stdin>", line 1, in ?
NameError: name 'fields' is not defined
>>>
```

Variáveis locais também não podem entrar em conflito com variáveis encontradas em outros lugares.
