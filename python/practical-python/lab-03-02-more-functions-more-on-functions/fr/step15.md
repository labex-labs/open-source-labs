# Exercice 3.5 : Effectuer des conversions de type

Modifiez la fonction `parse_csv()` dans le répertoire `/home/labex/project/fileparse_3.5.py` de sorte qu'elle permette facultativement d'appliquer des conversions de type aux données renvoyées. Par exemple :

```python
>>> portfolio = parse_csv('/home/labex/project/portfolio.csv', types=[str, int, float])
>>> portfolio
[{'name': 'AA','shares': 100, 'price': 32.2}, {'name': 'IBM','shares': 50, 'price': 91.1}, {'name': 'CAT','shares': 150, 'price': 83.44}, {'name': 'MSFT','shares': 200, 'price': 51.23}, {'name': 'GE','shares': 95, 'price': 40.37}, {'name': 'MSFT','shares': 50, 'price': 65.1}, {'name': 'IBM','shares': 100, 'price': 70.44}]

>>> shares_held = parse_csv('/home/labex/project/portfolio.csv', select=['name','shares'], types=[str, int])
>>> shares_held
[{'name': 'AA','shares': 100}, {'name': 'IBM','shares': 50}, {'name': 'CAT','shares': 150}, {'name': 'MSFT','shares': 200}, {'name': 'GE','shares': 95}, {'name': 'MSFT','shares': 50}, {'name': 'IBM','shares': 100}]
>>>
```

Vous avez déjà exploré ceci dans l'exercice 2.24. Vous devrez insérer le fragment de code suivant dans votre solution :

```python
...
if types:
    row = [func(val) for func, val in zip(types, row) ]
...
```
