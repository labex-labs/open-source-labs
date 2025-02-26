# Ejercicio 3.5: Realizar conversión de tipos

Modifica la función `parse_csv()` en el directorio `/home/labex/project/fileparse_3.5.py` de modo que opcionalmente permita que se apliquen conversiones de tipos a los datos devueltos. Por ejemplo:

```python
>>> portfolio = parse_csv('/home/labex/project/portfolio.csv', types=[str, int, float])
>>> portfolio
[{'name': 'AA','shares': 100, 'price': 32.2}, {'name': 'IBM','shares': 50, 'price': 91.1}, {'name': 'CAT','shares': 150, 'price': 83.44}, {'name': 'MSFT','shares': 200, 'price': 51.23}, {'name': 'GE','shares': 95, 'price': 40.37}, {'name': 'MSFT','shares': 50, 'price': 65.1}, {'name': 'IBM','shares': 100, 'price': 70.44}]

>>> shares_held = parse_csv('/home/labex/project/portfolio.csv', select=['name','shares'], types=[str, int])
>>> shares_held
[{'name': 'AA','shares': 100}, {'name': 'IBM','shares': 50}, {'name': 'CAT','shares': 150}, {'name': 'MSFT','shares': 200}, {'name': 'GE','shares': 95}, {'name': 'MSFT','shares': 50}, {'name': 'IBM','shares': 100}]
>>>
```

Ya exploraste esto en el Ejercicio 2.24. Necesitarás insertar el siguiente fragmento de código en tu solución:

```python
...
if types:
    row = [func(val) for func, val in zip(types, row) ]
...
```
