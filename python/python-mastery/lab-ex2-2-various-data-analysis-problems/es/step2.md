# Usando Comprensiones de Listas, Conjuntos y Diccionarios

Las comprensiones en Python son una forma realmente útil y concisa de crear nuevas colecciones basadas en otras existentes. Las colecciones en Python pueden ser listas, conjuntos o diccionarios, que son como contenedores que almacenan diferentes tipos de datos. Las comprensiones te permiten filtrar ciertos datos, transformarlos de alguna manera y organizarlos de forma más eficiente. En esta parte, usaremos nuestros datos de cartera para explorar cómo funcionan estas comprensiones.

Primero, necesitas abrir un terminal de Python, tal como lo hiciste en el paso anterior. Una vez abierto el terminal, ingresarás los siguientes ejemplos uno por uno. Este enfoque práctico te ayudará a entender cómo funcionan las comprensiones en la práctica.

## Comprensiones de Listas

Una comprensión de lista es una sintaxis especial en Python que crea una nueva lista. Lo hace aplicando una expresión a cada elemento de una colección existente.

Comencemos con un ejemplo. Primero, importaremos una función para leer nuestros datos de cartera. Luego, usaremos una comprensión de lista para filtrar ciertas acciones de la cartera.

```python
>>> from readport import read_portfolio
>>> portfolio = read_portfolio('/home/labex/project/portfolio.csv')

# Find all holdings with more than 100 shares
>>> large_holdings = [s for s in portfolio if s['shares'] > 100]
>>> print(large_holdings)
[{'name': 'CAT', 'shares': 150, 'price': 83.44}, {'name': 'MSFT', 'shares': 200, 'price': 51.23}]
```

En este código, primero importamos la función `read_portfolio` y la usamos para leer los datos de la cartera de un archivo CSV. Luego, la comprensión de lista `[s for s in portfolio if s['shares'] > 100]` recorre cada elemento `s` de la colección `portfolio`. Solo incluye el elemento `s` en la nueva lista `large_holdings` si el número de acciones de esa inversión es mayor a 100.

Las comprensiones de lista también se pueden usar para realizar cálculos. Aquí hay algunos ejemplos:

```python
# Calculate the total cost of each holding (shares * price)
>>> holding_costs = [s['shares'] * s['price'] for s in portfolio]
>>> print(holding_costs)
[3220.0, 4555.0, 12516.0, 10246.0, 3835.15, 3255.0, 7044.0]

# Calculate the total cost of the entire portfolio
>>> total_portfolio_cost = sum([s['shares'] * s['price'] for s in portfolio])
>>> print(total_portfolio_cost)
44671.15
```

En el primer ejemplo, la comprensión de lista `[s['shares'] * s['price'] for s in portfolio]` calcula el costo total de cada inversión multiplicando el número de acciones por el precio de cada elemento en la `portfolio`. En el segundo ejemplo, usamos la función `sum` junto con la comprensión de lista para calcular el costo total de la cartera completa.

## Comprensiones de Conjuntos

Una comprensión de conjunto se utiliza para crear un conjunto a partir de una colección existente. Un conjunto es una colección que solo contiene valores únicos.

Veamos cómo funciona con nuestros datos de cartera:

```python
# Find all unique stock names
>>> unique_stocks = {s['name'] for s in portfolio}
>>> print(unique_stocks)
{'MSFT', 'IBM', 'AA', 'GE', 'CAT'}
```

En este código, la comprensión de conjunto `{s['name'] for s in portfolio}` recorre cada elemento `s` de la `portfolio` y agrega el nombre de la acción (`s['name']`) al conjunto `unique_stocks`. Dado que los conjuntos solo almacenan valores únicos, terminamos con una lista de todas las diferentes acciones en nuestra cartera sin duplicados.

## Comprensiones de Diccionarios

Una comprensión de diccionario crea un nuevo diccionario aplicando expresiones para crear pares clave - valor.

Aquí hay un ejemplo de cómo usar una comprensión de diccionario para contar el número total de acciones de cada acción en nuestra cartera:

```python
# Create a dictionary to count total shares for each stock
>>> totals = {s['name']: 0 for s in portfolio}
>>> for s in portfolio:
...     totals[s['name']] += s['shares']
...
>>> print(totals)
{'AA': 100, 'IBM': 150, 'CAT': 150, 'MSFT': 250, 'GE': 95}
```

En la primera línea, la comprensión de diccionario `{s['name']: 0 for s in portfolio}` crea un diccionario donde cada nombre de acción (`s['name']`) es una clave, y el valor inicial de cada clave es 0. Luego, usamos un bucle `for` para recorrer cada elemento de la `portfolio`. Para cada elemento, agregamos el número de acciones (`s['shares']`) al valor correspondiente en el diccionario `totals`.

Estas comprensiones son muy poderosas porque te permiten transformar y analizar datos con solo unas pocas líneas de código. Son una gran herramienta para tener en tu kit de herramientas de programación en Python.
