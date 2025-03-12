# Trabajando con Diccionarios y Datos CSV

Comencemos examinando un simple conjunto de datos sobre carteras de acciones. En este paso, aprenderás cómo leer datos de un archivo CSV y almacenarlos en un formato estructurado utilizando diccionarios.

Un archivo CSV (Comma-Separated Values, Valores Separados por Comas) es una forma común de almacenar datos tabulares, donde cada línea representa una fila y los valores están separados por comas. Los diccionarios en Python son una poderosa estructura de datos que te permite almacenar pares clave - valor. Al utilizar diccionarios, podemos organizar los datos del archivo CSV de una manera más significativa.

Primero, crea un nuevo archivo de Python en el WebIDE siguiendo estos pasos:

1. Haz clic en el botón "Nuevo Archivo" en el WebIDE.
2. Nombrar el archivo `readport.py`.
3. Copia y pega el siguiente código en el archivo:

```python
# readport.py

import csv

# A function that reads a file into a list of dictionaries
def read_portfolio(filename):
    portfolio = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)   # Skip the header row
        for row in rows:
            record = {
                'name': row[0],
                'shares': int(row[1]),
                'price': float(row[2])
            }
            portfolio.append(record)
    return portfolio
```

Este código define una función `read_portfolio` que realiza varias tareas importantes:

1. Abre un archivo CSV especificado por el parámetro `filename`. La función `open` se utiliza para acceder al archivo, y la declaración `with` asegura que el archivo se cierre adecuadamente después de terminar de leerlo.
2. Omite la fila de encabezado. La fila de encabezado generalmente contiene los nombres de las columnas en el archivo CSV. Usamos `next(rows)` para mover el iterador a la siguiente fila, saltando efectivamente el encabezado.
3. Para cada fila de datos, crea un diccionario. Las claves del diccionario son 'name', 'shares' y 'price'. Estas claves nos ayudarán a acceder a los datos de una manera más intuitiva.
4. Convierte las acciones en enteros y los precios en números de punto flotante. Esto es importante porque los datos leídos del archivo CSV están inicialmente en formato de cadena, y necesitamos valores numéricos para realizar cálculos.
5. Agrega cada diccionario a una lista llamada `portfolio`. Esta lista contendrá todos los registros del archivo CSV.
6. Finalmente, devuelve la lista completa de diccionarios.

Ahora, creemos un archivo para los datos de transporte público. Crea un nuevo archivo llamado `readrides.py` con este contenido:

```python
# readrides.py

import csv

def read_rides_as_dicts(filename):
    """
    Read the CTA bus data as a list of dictionaries
    """
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)   # Skip header
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = {
                'route': route,
                'date': date,
                'daytype': daytype,
                'rides': rides
            }
            records.append(record)
    return records
```

La función `read_rides_as_dicts` funciona de manera similar a la función `read_portfolio`. Lee un archivo CSV relacionado con los datos de autobuses de la CTA (Chicago Transit Authority), omite la fila de encabezado, crea un diccionario para cada fila de datos y almacena estos diccionarios en una lista.

Ahora, probemos la función `read_portfolio` abriendo un terminal en el WebIDE:

1. Haz clic en el menú "Terminal" y selecciona "Nuevo Terminal".
2. Inicia el intérprete de Python escribiendo `python3`.
3. Ejecuta los siguientes comandos:

```python
>>> from readport import read_portfolio
>>> portfolio = read_portfolio('/home/labex/project/portfolio.csv')
>>> from pprint import pprint
>>> pprint(portfolio)
[{'name': 'AA', 'price': 32.2, 'shares': 100},
 {'name': 'IBM', 'price': 91.1, 'shares': 50},
 {'name': 'CAT', 'price': 83.44, 'shares': 150},
 {'name': 'MSFT', 'price': 51.23, 'shares': 200},
 {'name': 'GE', 'price': 40.37, 'shares': 95},
 {'name': 'MSFT', 'price': 65.1, 'shares': 50},
 {'name': 'IBM', 'price': 70.44, 'shares': 100}]
```

La función `pprint` (impresión bonita) se utiliza aquí para mostrar los datos en un formato más legible. Cada elemento de la lista es un diccionario que representa una acción en la cartera. El diccionario tiene las siguientes claves:

- Un símbolo de acción (`name`): Esta es la abreviatura utilizada para identificar la acción.
- Número de acciones poseídas (`shares`): Esto indica cuántas acciones de la empresa se poseen.
- Precio de compra por acción (`price`): Este es el precio al que se compró cada acción.

Observa que algunas acciones como 'MSFT' e 'IBM' aparecen varias veces. Estas representan diferentes compras de la misma acción, que podrían haberse realizado en diferentes momentos y precios.
