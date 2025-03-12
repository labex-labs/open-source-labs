# Expresiones generadoras y eficiencia de memoria

En este paso, exploraremos las expresiones generadoras. Estas son increíblemente útiles cuando se trabaja con grandes conjuntos de datos en Python. Pueden hacer que tu código sea mucho más eficiente en términos de memoria, lo cual es crucial cuando se maneja una gran cantidad de datos.

## Comprendiendo las expresiones generadoras

Una expresión generadora es similar a una comprensión de lista, pero hay una diferencia clave. Cuando se utiliza una comprensión de lista, Python crea una lista con todos los resultados de una vez. Esto puede ocupar mucha memoria, especialmente si se está trabajando con un gran conjunto de datos. Por otro lado, una expresión generadora produce resultados uno a la vez según se necesitan. Esto significa que no necesita almacenar todos los resultados en memoria de una vez, lo que puede ahorrar una cantidad significativa de memoria.

Veamos un ejemplo sencillo para ver cómo funciona esto:

```python
# Start a new Python session if needed
# python3

# List comprehension (creates a list in memory)
nums = [1, 2, 3, 4, 5]
squares_list = [x*x for x in nums]
print(squares_list)

# Generator expression (creates a generator object)
squares_gen = (x*x for x in nums)
print(squares_gen)  # This doesn't print the values, just the generator object

# Iterate through the generator to get values
for n in squares_gen:
    print(n)
```

Cuando se ejecuta este código, se verá la siguiente salida:

```
[1, 4, 9, 16, 25]
<generator object <genexpr> at 0x7f...>
1
4
9
16
25
```

Una cosa importante a tener en cuenta sobre los generadores es que solo se pueden iterar una vez. Una vez que se han recorrido todos los valores de un generador, se agota y no se pueden obtener los valores de nuevo.

```python
# Try to iterate again over the same generator
for n in squares_gen:
    print(n)  # Nothing will be printed, as the generator is already exhausted
```

También se pueden obtener valores manualmente de un generador uno a la vez utilizando la función `next()`.

```python
# Create a fresh generator
squares_gen = (x*x for x in nums)

# Get values one by one
print(next(squares_gen))  # 1
print(next(squares_gen))  # 4
print(next(squares_gen))  # 9
```

Cuando no hay más valores en el generador, llamar a `next()` generará una excepción `StopIteration`.

## Funciones generadoras con `yield`

Para una lógica de generador más compleja, se pueden escribir funciones generadoras utilizando la declaración `yield`. Una función generadora es un tipo especial de función que utiliza `yield` para devolver valores uno a la vez en lugar de devolver un solo resultado de una vez.

```python
def squares(nums):
    for x in nums:
        yield x*x

# Use the generator function
for n in squares(nums):
    print(n)
```

Cuando se ejecuta este código, se verá la siguiente salida:

```
1
4
9
16
25
```

## Reduciendo el uso de memoria con expresiones generadoras

Ahora, veamos cómo las expresiones generadoras pueden ahorrar memoria cuando se trabaja con grandes conjuntos de datos. Utilizaremos el archivo de datos de autobuses CTA, que es bastante grande.

Primero, probemos un enfoque que consume mucha memoria:

```python
import tracemalloc
tracemalloc.start()

import readrides
rows = readrides.read_rides_as_dicts('ctabus.csv')
rt22 = [row for row in rows if row['route'] == '22']
max_row = max(rt22, key=lambda row: int(row['rides']))
print(max_row)

# Check memory usage
current, peak = tracemalloc.get_traced_memory()
print(f"Current memory usage: {current / 1024 / 1024:.2f} MB")
print(f"Peak memory usage: {peak / 1024 / 1024:.2f} MB")
```

Ahora, salga de Python y reinícielo para comparar con un enfoque basado en generadores:

```bash
exit() python3
```

```python
import tracemalloc
tracemalloc.start()

import csv
f = open('ctabus.csv')
f_csv = csv.reader(f)
headers = next(f_csv)

# Use generator expressions for all operations
rows = (dict(zip(headers, row)) for row in f_csv)
rt22 = (row for row in rows if row['route'] == '22')
max_row = max(rt22, key=lambda row: int(row['rides']))
print(max_row)

# Check memory usage
current, peak = tracemalloc.get_traced_memory()
print(f"Current memory usage: {current / 1024 / 1024:.2f} MB")
print(f"Peak memory usage: {peak / 1024 / 1024:.2f} MB")
```

Debería notar una diferencia significativa en el uso de memoria entre estos dos enfoques. El enfoque basado en generadores procesa los datos de forma incremental sin cargar todo en memoria de una vez, lo que es mucho más eficiente en términos de memoria.

## Expresiones generadoras con funciones de reducción

Las expresiones generadoras son particularmente útiles cuando se combinan con funciones como `sum()`, `min()`, `max()`, `any()` y `all()` que procesan una secuencia completa y producen un solo resultado.

Veamos algunos ejemplos:

```python
from readport import read_portfolio
portfolio = read_portfolio('portfolio.csv')

# Calculate the total value of the portfolio
total_value = sum(s['shares']*s['price'] for s in portfolio)
print(f"Total portfolio value: {total_value}")

# Find the minimum number of shares in any holding
min_shares = min(s['shares'] for s in portfolio)
print(f"Minimum shares in any holding: {min_shares}")

# Check if any stock is IBM
has_ibm = any(s['name'] == 'IBM' for s in portfolio)
print(f"Portfolio contains IBM: {has_ibm}")

# Check if all stocks are IBM
all_ibm = all(s['name'] == 'IBM' for s in portfolio)
print(f"All stocks are IBM: {all_ibm}")

# Count IBM shares
ibm_shares = sum(s['shares'] for s in portfolio if s['name'] == 'IBM')
print(f"Total IBM shares: {ibm_shares}")
```

Las expresiones generadoras también son útiles para operaciones de cadenas. Aquí está cómo unir valores en una tupla:

```python
s = ('GOOG', 100, 490.10)
# This would fail: ','.join(s)
# Use a generator expression to convert all items to strings
joined = ','.join(str(x) for x in s)
print(joined)  # Output: 'GOOG,100,490.1'
```

La principal ventaja de utilizar expresiones generadoras en estos ejemplos es que no se crean listas intermedias, lo que resulta en un código más eficiente en términos de memoria.
