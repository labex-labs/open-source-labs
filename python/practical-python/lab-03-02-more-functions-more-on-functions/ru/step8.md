# Локальные переменные

Переменные, присвоенные внутри функций, являются приватными.

```python
def read_portfolio(filename):
    portfolio = []
    for line in open(filename):
        fields = line.split(',')
        s = (fields[0], int(fields[1]), float(fields[2]))
        portfolio.append(s)
    return portfolio
```

В этом примере `filename`, `portfolio`, `line`, `fields` и `s` - это локальные переменные. Эти переменные не сохраняются и не доступны после вызова функции.

```python
>>> stocks = read_portfolio('portfolio.csv')
>>> fields
Traceback (most recent call last):
File "<stdin>", line 1, in?
NameError: name 'fields' is not defined
>>>
```

Локальные переменные также не могут конфликтовать с переменными, найденными в других местах.
