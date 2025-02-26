# Comprehensiones

Las comprensiones de listas, conjuntos y diccionarios pueden ser una herramienta útil para manipular datos. Por ejemplo, prueba estas operaciones:

```python
>>> # Encuentra todas las inversiones con más de 100 acciones
>>> [s for s in portfolio if s['shares'] > 100]
[{'name': 'CAT','shares': 150, 'price': 83.44},
 {'name': 'MSFT','shares': 200, 'price': 51.23}]

>>> # Calcula el costo total (acciones * precio)
>>> sum([s['shares']*s['price'] for s in portfolio])
44671.15
>>>

>>> # Encuentra todos los nombres de acciones únicos (conjunto)
>>> { s['name'] for s in portfolio }
{'MSFT', 'IBM', 'AA', 'GE', 'CAT'}
>>>

>>> # Cuenta el total de acciones de cada acción
>>> totals = { s['name']: 0 for s in portfolio }
>>> for s in portfolio:
        totals[s['name']] += s['shares']

>>> totals
{'AA': 100, 'IBM': 150, 'CAT': 150, 'MSFT': 250, 'GE': 95}
>>>
```
