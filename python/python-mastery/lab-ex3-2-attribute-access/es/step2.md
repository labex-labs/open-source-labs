# Usando `getattr()` para el procesamiento genérico de objetos

La función `getattr()` es una herramienta poderosa en Python que te permite acceder a los atributos de un objeto de forma dinámica. Esto es especialmente útil cuando quieres procesar objetos de manera genérica. En lugar de escribir código específico para un tipo de objeto en particular, puedes usar `getattr()` para trabajar con cualquier objeto que tenga los atributos requeridos. Esta flexibilidad hace que tu código sea más reutilizable y adaptable.

## Procesando múltiples atributos

Comencemos aprendiendo cómo acceder a múltiples atributos de un objeto utilizando la función `getattr()`. Este es un escenario común cuando necesitas extraer información específica de un objeto.

Primero, abre una shell interactiva de Python si cerraste la anterior. Puedes hacer esto ejecutando el siguiente comando en tu terminal:

```python
# Open a Python interactive shell if you closed the previous one
python3
```

A continuación, importaremos la clase `Stock` y crearemos un objeto `Stock`. La clase `Stock` representa una acción con atributos como `name`, `shares` y `price`.

```python
# Import the Stock class and create a stock object
from stock import Stock
s = Stock('GOOG', 100, 490.1)
```

Ahora, definiremos una lista de nombres de atributos a los que queremos acceder. Esta lista nos ayudará a iterar sobre los atributos y a imprimir sus valores.

```python
# Define a list of attribute names
fields = ['name', 'shares', 'price']
```

Finalmente, usaremos un bucle `for` para iterar sobre la lista de nombres de atributos y acceder a cada atributo utilizando `getattr()`. Imprimiremos el nombre del atributo y su valor en cada iteración.

```python
# Access each attribute using getattr()
for name in fields:
    print(f"{name}: {getattr(s, 'name')}" if name == 'name' else f"{name}: {getattr(s, name)}")
```

Cuando ejecutes este código, verás la siguiente salida:

```
name: GOOG
shares: 100
price: 490.1
```

Esta salida muestra que pudimos acceder e imprimir los valores de múltiples atributos del objeto `Stock` utilizando la función `getattr()`.

## Valores predeterminados con `getattr()`

La función `getattr()` también ofrece una característica útil: la posibilidad de especificar un valor predeterminado si el atributo al que estás intentando acceder no existe. Esto puede evitar que tu código lance un `AttributeError` y hacerlo más robusto.

Veamos cómo funciona esto. Primero, intentaremos acceder a un atributo que no existe en el objeto `Stock`. Usaremos `getattr()` y proporcionaremos un valor predeterminado de `'N/A'`.

```python
# Try to access an attribute that doesn't exist
print(getattr(s, 'symbol', 'N/A'))  # Output: 'N/A'
```

En este caso, dado que el atributo `symbol` no existe en el objeto `Stock`, `getattr()` devuelve el valor predeterminado `'N/A'`.

Ahora, comparemos esto con acceder a un atributo existente. Accederemos al atributo `name`, que sí existe en el objeto `Stock`.

```python
# Compare with an existing attribute
print(getattr(s, 'name', 'N/A'))    # Output: 'GOOG'
```

Aquí, `getattr()` devuelve el valor real del atributo `name`, que es `'GOOG'`.

## Procesando una colección de objetos

La función `getattr()` se vuelve aún más poderosa cuando necesitas procesar una colección de objetos. Veamos cómo podemos usarla para procesar una cartera de acciones.

Primero, importaremos la función `read_portfolio` del módulo `stock`. Esta función lee una cartera de acciones desde un archivo CSV y devuelve una lista de objetos `Stock`.

```python
# Import the portfolio reading function
from stock import read_portfolio
```

A continuación, usaremos la función `read_portfolio` para leer la cartera desde un archivo CSV llamado `portfolio.csv`.

```python
# Read the portfolio from CSV file
portfolio = read_portfolio('portfolio.csv')
```

Finalmente, usaremos un bucle `for` para iterar sobre la lista de objetos `Stock` en la cartera. Para cada acción, usaremos `getattr()` para acceder a los atributos `name` y `shares` e imprimir sus valores.

```python
# Print the name and shares of each stock
for stock in portfolio:
    print(f"Stock: {getattr(stock, 'name')}, Shares: {getattr(stock, 'shares')}")
```

Este enfoque hace que tu código sea más flexible porque puedes trabajar con nombres de atributos como cadenas. Estas cadenas se pueden pasar como argumentos o almacenar en estructuras de datos, lo que te permite cambiar fácilmente los atributos a los que quieres acceder sin modificar la lógica central de tu código.
