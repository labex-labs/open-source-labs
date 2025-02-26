# Variables locales

Las variables asignadas dentro de las funciones son privadas.

```python
def read_portfolio(filename):
    portfolio = []
    for line in open(filename):
        fields = line.split(',')
        s = (fields[0], int(fields[1]), float(fields[2]))
        portfolio.append(s)
    return portfolio
```

En este ejemplo, `filename`, `portfolio`, `line`, `fields` y `s` son variables locales. Esas variables no se conservan ni son accesibles después de la llamada a la función.

```python
>>> stocks = read_portfolio('portfolio.csv')
>>> fields
Traceback (most recent call last):
File "<stdin>", line 1, in?
NameError: name 'fields' is not defined
>>>
```

Las variables locales también no pueden entrar en conflicto con las variables encontradas en otros lugares.
