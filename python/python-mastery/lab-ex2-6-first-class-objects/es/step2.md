# Creando una Función de Utilidad para el Procesamiento de CSV

Ahora que entendemos cómo los objetos de primera clase de Python pueden ayudarnos con la conversión de datos, vamos a crear una función de utilidad reutilizable. Esta función leerá datos CSV y los transformará en una lista de diccionarios. Esta es una operación muy útil porque los archivos CSV se utilizan comúnmente para almacenar datos tabulares, y convertir estos archivos en una lista de diccionarios facilita el trabajo con los datos en Python.

## Creando la Utilidad de Lectura de CSV

Primero, abre el WebIDE. Una vez abierto, navega hasta el directorio del proyecto y crea un nuevo archivo llamado `reader.py`. En este archivo, definiremos una función que lee datos CSV y aplica conversiones de tipo. Las conversiones de tipo son importantes porque los datos en un archivo CSV generalmente se leen como cadenas, pero es posible que necesitemos diferentes tipos de datos, como enteros o números de punto flotante, para un procesamiento posterior.

Agrega el siguiente código a `reader.py`:

```python
import csv

def read_csv_as_dicts(filename, types):
    """
    Read a CSV file into a list of dictionaries, converting each field according
    to the types provided.

    Parameters:
    filename (str): Name of the CSV file to read
    types (list): List of type conversion functions for each column

    Returns:
    list: List of dictionaries representing the CSV data
    """
    records = []
    with open(filename, 'r') as f:
        rows = csv.reader(f)
        headers = next(rows)  # Get the column headers

        for row in rows:
            # Apply type conversions to each value in the row
            converted_row = [func(val) for func, val in zip(types, row)]

            # Create a dictionary mapping headers to converted values
            record = dict(zip(headers, converted_row))
            records.append(record)

    return records
```

Esta función primero abre el archivo CSV especificado. Luego lee los encabezados del archivo CSV, que son los nombres de las columnas. Después de eso, recorre cada fila del archivo. Para cada valor en la fila, aplica la función de conversión de tipo correspondiente de la lista `types`. Finalmente, crea un diccionario donde las claves son los encabezados de las columnas y los valores son los datos convertidos, y agrega este diccionario a la lista `records`. Una vez que se han procesado todas las filas, devuelve la lista `records`.

## Probando la Función de Utilidad

Probemos nuestra función de utilidad. Primero, abre una terminal y inicia un intérprete de Python escribiendo:

```bash
python3
```

Ahora que estamos en el intérprete de Python, podemos usar nuestra función para leer los datos de la cartera. Los datos de la cartera son un archivo CSV que contiene información sobre acciones, como el nombre de la acción, el número de acciones y el precio.

```python
import reader
portfolio = reader.read_csv_as_dicts('portfolio.csv', [str, int, float])
for record in portfolio[:3]:  # Show the first 3 records
    print(record)
```

Cuando ejecutes este código, deberías ver una salida similar a:

```
{'name': 'AA', 'shares': 100, 'price': 32.2}
{'name': 'IBM', 'shares': 50, 'price': 91.1}
{'name': 'CAT', 'shares': 150, 'price': 83.44}
```

Esta salida muestra los tres primeros registros de los datos de la cartera, con los tipos de datos convertidos correctamente.

Probemos también nuestra función con los datos de autobuses del CTA. Los datos de autobuses del CTA son otro archivo CSV que contiene información sobre rutas de autobús, fechas, tipos de día y el número de viajes.

```python
rows = reader.read_csv_as_dicts('ctabus.csv', [str, str, str, int])
print(f"Total rows: {len(rows)}")
print("First row:", rows[0])
```

La salida debería ser algo como:

```
Total rows: 577563
First row: {'route': '3', 'date': '01/01/2001', 'daytype': 'U', 'rides': 7354}
```

Esto muestra que nuestra función puede manejar diferentes archivos CSV y aplicar las conversiones de tipo adecuadas.

Para salir del intérprete de Python, escribe:

```python
exit()
```

Ahora has creado una función de utilidad reutilizable que puede leer cualquier archivo CSV y aplicar las conversiones de tipo adecuadas. Esto demuestra el poder de los objetos de primera clase de Python y cómo se pueden utilizar para crear código flexible y reutilizable.
