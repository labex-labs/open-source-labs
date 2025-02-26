# Variables locales

Les variables assignées à l'intérieur des fonctions sont privées.

```python
def read_portfolio(filename):
    portfolio = []
    for line in open(filename):
        fields = line.split(',')
        s = (fields[0], int(fields[1]), float(fields[2]))
        portfolio.append(s)
    return portfolio
```

Dans cet exemple, `filename`, `portfolio`, `line`, `fields` et `s` sont des variables locales. Ces variables ne sont pas conservées ni accessibles après l'appel de la fonction.

```python
>>> stocks = read_portfolio('portfolio.csv')
>>> fields
Traceback (most recent call last):
File "<stdin>", line 1, in?
NameError: name 'fields' is not defined
>>>
```

Les variables locales ne peuvent également pas entrer en conflit avec les variables trouvées ailleurs.
