# Creando una función de utilidad para el análisis sintáctico

Crea un nuevo archivo `reader.py`. En ese archivo, define una función de utilidad `read_csv_as_dicts()` que lee un archivo de datos CSV en una lista de diccionarios donde el usuario especifica las conversiones de tipo para cada columna.

Así es como debería funcionar:

```python
>>> import reader
>>> portfolio = reader.read_csv_as_dicts('portfolio.csv', [str,int,float])
>>> for s in portfolio:
         print(s)

{'name': 'AA','shares': 100, 'price': 32.2}
{'name': 'IBM','shares': 50, 'price': 91.1}
{'name': 'CAT','shares': 150, 'price': 83.44}
{'name': 'MSFT','shares': 200, 'price': 51.23}
{'name': 'GE','shares': 95, 'price': 40.37}
{'name': 'MSFT','shares': 50, 'price': 65.1}
{'name': 'IBM','shares': 100, 'price': 70.44}
>>>
```

O, si quisieras leer los datos de CTA:

```python
>>> rows = reader.read_csv_as_dicts('ctabus.csv', [str,str,str,int])
>>> len(rows)
577563
>>> rows[0]
{'daytype': 'U', 'route': '3', 'rides': 7354, 'date': '01/01/2001'}
>>>
```
