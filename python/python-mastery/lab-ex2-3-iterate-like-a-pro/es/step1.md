# Iteración básica y desempaquetado de secuencias

En este paso, exploraremos la iteración básica utilizando bucles `for` y el desempaquetado de secuencias en Python. La iteración es un concepto fundamental en la programación, que te permite recorrer cada elemento de una secuencia uno por uno. El desempaquetado de secuencias, por otro lado, te permite asignar los elementos individuales de una secuencia a variables de manera conveniente.

## Cargar datos desde un archivo CSV

Comencemos cargando algunos datos desde un archivo CSV. CSV (Comma-Separated Values, Valores Separados por Comas) es un formato de archivo común utilizado para almacenar datos tabulares. Para comenzar, necesitamos abrir un terminal en el WebIDE y iniciar el intérprete de Python. Esto nos permitirá ejecutar código Python de forma interactiva.

```bash
cd ~/project
python3
```

Ahora que estamos en el intérprete de Python, podemos ejecutar el siguiente código Python para leer datos del archivo `portfolio.csv`. Primero, importamos el módulo `csv`, que proporciona funcionalidades para trabajar con archivos CSV. Luego, abrimos el archivo y creamos un objeto `csv.reader` para leer los datos. Utilizamos la función `next` para obtener los encabezados de las columnas y convertimos el resto de los datos en una lista. Finalmente, utilizamos la función `pprint` del módulo `pprint` para imprimir las filas en un formato más legible.

```python
import csv

f = open('portfolio.csv')
f_csv = csv.reader(f)
headers = next(f_csv)    # Get the column headers
rows = list(f_csv)       # Convert the remaining data to a list
from pprint import pprint
pprint(rows)             # Pretty print the rows
```

Deberías ver una salida similar a esta:

```
[['AA', '100', '32.20'],
 ['IBM', '50', '91.10'],
 ['CAT', '150', '83.44'],
 ['MSFT', '200', '51.23'],
 ['GE', '95', '40.37'],
 ['MSFT', '50', '65.10'],
 ['IBM', '100', '70.44']]
```

## Iteración básica con bucles `for`

La declaración `for` en Python se utiliza para iterar sobre cualquier secuencia de datos, como una lista, tupla o cadena. En nuestro caso, la utilizaremos para iterar sobre las filas de datos que cargamos desde el archivo CSV.

```python
for row in rows:
    print(row)
```

Este código recorrerá cada fila de la lista `rows` e imprimirá cada una. Verás cada fila de datos de nuestro archivo CSV impresa una por una.

```
['AA', '100', '32.20']
['IBM', '50', '91.10']
['CAT', '150', '83.44']
['MSFT', '200', '51.23']
['GE', '95', '40.37']
['MSFT', '50', '65.10']
['IBM', '100', '70.44']
```

## Desempaquetado de secuencias en bucles

Python te permite desempaquetar secuencias directamente en un bucle `for`. Esto es muy útil cuando conoces la estructura de cada elemento de la secuencia. En nuestro caso, cada fila de la lista `rows` contiene tres elementos: un nombre, el número de acciones y el precio. Podemos desempaquetar estos elementos directamente en el bucle `for`.

```python
for name, shares, price in rows:
    print(name, shares, price)
```

Este código desempaquetará cada fila en las variables `name`, `shares` y `price`, y luego las imprimirá. Verás los datos impresos en un formato más legible.

```
AA 100 32.20
IBM 50 91.10
CAT 150 83.44
MSFT 200 51.23
GE 95 40.37
MSFT 50 65.10
IBM 100 70.44
```

Si no necesitas algunos valores, puedes utilizar `_` como un marcador de posición para indicar que no te importan esos valores. Por ejemplo, si solo quieres imprimir el nombre y el precio, puedes utilizar el siguiente código:

```python
for name, _, price in rows:
    print(name, price)
```

Este código ignorará el segundo elemento de cada fila e imprimirá solo el nombre y el precio.

```
AA 32.20
IBM 91.10
CAT 83.44
MSFT 51.23
GE 40.37
MSFT 65.10
IBM 70.44
```

## Desempaquetado extendido con el operador `*`

Para un desempaquetado más avanzado, puedes utilizar el operador `*` como un comodín. Esto te permite recopilar múltiples elementos en una lista. Agrupemos nuestros datos por nombre utilizando esta técnica.

```python
from collections import defaultdict

byname = defaultdict(list)
for name, *data in rows:
    byname[name].append(data)

# Print the data for IBM
print(byname['IBM'])

# Iterate through IBM's data
for shares, price in byname['IBM']:
    print(shares, price)
```

En este código, primero importamos la clase `defaultdict` del módulo `collections`. Un `defaultdict` es un diccionario que crea automáticamente un nuevo valor (en este caso, una lista vacía) si la clave no existe. Luego, utilizamos el operador `*` para recopilar todos los elementos excepto el primero en una lista llamada `data`. Almacenamos esta lista en el diccionario `byname`, agrupada por el nombre. Finalmente, imprimimos los datos de IBM y los recorremos para imprimir el número de acciones y el precio.

Salida:

```
[['50', '91.10'], ['100', '70.44']]
50 91.10
100 00.44
```

En este ejemplo, `*data` recopila todos los elementos excepto el primero en una lista, que luego almacenamos en un diccionario agrupado por nombre. Esta es una técnica poderosa para manejar datos con secuencias de longitud variable.
