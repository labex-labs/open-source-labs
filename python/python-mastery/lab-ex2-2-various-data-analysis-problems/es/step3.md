# Explorando el Módulo `collections`

En Python, los contenedores incorporados como listas, diccionarios y conjuntos son muy útiles. Sin embargo, el módulo `collections` de Python va un paso más allá al proporcionar tipos de datos de contenedores especializados que extienden la funcionalidad de estos contenedores incorporados. Echemos un vistazo más de cerca a algunos de estos tipos de datos útiles.

Continuarás trabajando en tu terminal de Python y seguirás los ejemplos a continuación.

## `Counter`

La clase `Counter` es una subclase del diccionario. Su propósito principal es contar objetos hashables. Ofrece una forma conveniente de contar elementos y admite una variedad de operaciones.

Primero, necesitamos importar la clase `Counter` y una función para leer una cartera. Luego, leeremos una cartera desde un archivo CSV.

```python
>>> from collections import Counter
>>> from readport import read_portfolio
>>> portfolio = read_portfolio('/home/labex/project/portfolio.csv')

```

Ahora, crearemos un objeto `Counter` para contar el número de acciones de cada acción por su nombre.

```python
# Create a counter to count shares by stock name
>>> totals = Counter()
>>> for s in portfolio:
...     totals[s['name']] += s['shares']
...
>>> print(totals)
Counter({'MSFT': 250, 'IBM': 150, 'CAT': 150, 'AA': 100, 'GE': 95})
```

Una de las grandes características del objeto `Counter` es que inicializa automáticamente nuevas claves con un recuento de 0. Esto significa que no tienes que comprobar si una clave existe antes de incrementar su recuento, lo que simplifica el código para acumular recuentos.

Los `Counter` también vienen con métodos especiales. Por ejemplo, el método `most_common()` es muy útil para el análisis de datos.

```python
# Get the two stocks with the most shares
>>> most_common_stocks = totals.most_common(2)
>>> print(most_common_stocks)
[('MSFT', 250), ('IBM', 150)]
```

Además, los `Counter` se pueden combinar utilizando operaciones aritméticas.

```python
# Create another counter
>>> more = Counter()
>>> more['IBM'] = 75
>>> more['AA'] = 200
>>> more['ACME'] = 30
>>> print(more)
Counter({'AA': 200, 'IBM': 75, 'ACME': 30})

# Add two counters together
>>> combined = totals + more
>>> print(combined)
Counter({'AA': 300, 'MSFT': 250, 'IBM': 225, 'CAT': 150, 'GE': 95, 'ACME': 30})
```

## `defaultdict`

El `defaultdict` es similar a un diccionario regular, pero tiene una característica única. Proporciona un valor predeterminado para las claves que aún no existen. Esto puede simplificar tu código, ya que ya no necesitas comprobar si una clave existe antes de usarla.

```python
>>> from collections import defaultdict

# Group portfolio entries by stock name
>>> byname = defaultdict(list)
>>> for s in portfolio:
...     byname[s['name']].append(s)
...
>>> print(byname['IBM'])
[{'name': 'IBM', 'shares': 50, 'price': 91.1}, {'name': 'IBM', 'shares': 100, 'price': 70.44}]
>>> print(byname['AA'])
[{'name': 'AA', 'shares': 100, 'price': 32.2}]
```

Cuando creas un `defaultdict(list)`, automáticamente crea una nueva lista vacía para cada nueva clave. Entonces, puedes agregar directamente a un valor de una clave incluso si la clave no existía antes. Esto elimina la necesidad de comprobar si la clave existe y crear una lista vacía manualmente.

También puedes usar otras funciones de fábrica predeterminadas. Por ejemplo, puedes usar `int`, `float` o incluso tu propia función personalizada.

```python
# Use defaultdict with int to count items
>>> word_counts = defaultdict(int)
>>> words = ['apple', 'orange', 'banana', 'apple', 'orange', 'apple']
>>> for word in words:
...     word_counts[word] += 1
...
>>> print(word_counts)
defaultdict(<class 'int'>, {'apple': 3, 'orange': 2, 'banana': 1})
```

Estos tipos de contenedores especializados del módulo `collections` pueden hacer que tu código sea más conciso y eficiente cuando trabajas con datos.
