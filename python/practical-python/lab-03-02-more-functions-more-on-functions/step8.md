# Local Variables

Variables assigned inside functions are private.

```python
def read_portfolio(filename):
    portfolio = []
    for line in open(filename):
        fields = line.split(',')
        s = (fields[0], int(fields[1]), float(fields[2]))
        portfolio.append(s)
    return portfolio
```

In this example, `filename`, `portfolio`, `line`, `fields` and `s` are local variables.
Those variables are not retained or accessible after the function call.

```python
>>> stocks = read_portfolio('portfolio.csv')
>>> fields
Traceback (most recent call last):
File "<stdin>", line 1, in ?
NameError: name 'fields' is not defined
>>>
```

Locals also can't conflict with variables found elsewhere.
