# Collections

El módulo `collections` tiene una variedad de clases para manipulación de datos más especializada. Por ejemplo, el último ejemplo podría resolverse con un `Counter` de la siguiente manera:

```python
>>> from collections import Counter
>>> totals = Counter()
>>> for s in portfolio:
        totals[s['name']] += s['shares']

>>> totals
Counter({'MSFT': 250, 'IBM': 150, 'CAT': 150, 'AA': 100, 'GE': 95})
>>>
```

Los contadores son interesantes porque admiten otros tipos de operaciones como clasificación y matemáticas. Por ejemplo:

```python
>>> # Obtén las dos inversiones más comunes
>>> totals.most_common(2)
[('MSFT', 250), ('IBM', 150)]
>>>

>>> # Sumar contadores
>>> more = Counter()
>>> more['IBM'] = 75
>>> more['AA'] = 200
>>> more['ACME'] = 30
>>> more
Counter({'AA': 200, 'IBM': 75, 'ACME': 30})
>>> totals
Counter({'MSFT': 250, 'IBM': 150, 'CAT': 150, 'AA': 100, 'GE': 95})
>>> totals + more
Counter({'AA': 300, 'MSFT': 250, 'IBM': 225, 'CAT': 150, 'GE': 95, 'ACME': 30})
>>>
```

El objeto `defaultdict` se puede utilizar para agrupar datos. Por ejemplo, supongamos que quieres facilitar la búsqueda de todas las entradas coincidentes para un nombre dado, como IBM. Prueba esto:

```python
>>> from collections import defaultdict
>>> byname = defaultdict(list)
>>> for s in portfolio:
        byname[s['name']].append(s)

>>> byname['IBM']
[{'name': 'IBM','shares': 50, 'price': 91.1}, {'name': 'IBM','shares': 100, 'price': 70.44}]
>>> byname['AA']
[{'name': 'AA','shares': 100, 'price': 32.2}]
>>>
```

La característica clave que hace que esto funcione es que un `defaultdict` inicializa automáticamente los elementos para ti, lo que permite combinar la inserción de un nuevo elemento y una operación `append()`.
