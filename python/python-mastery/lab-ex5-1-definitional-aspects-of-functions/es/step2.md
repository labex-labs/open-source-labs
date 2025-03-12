# Creando las funciones básicas de lectura de archivos CSV

Comencemos creando un archivo `reader.py` con dos funciones básicas para leer datos de archivos CSV. Estas funciones nos ayudarán a manejar archivos CSV de diferentes maneras, como convertir los datos en diccionarios o instancias de clase.

Primero, necesitamos entender qué es un archivo CSV. CSV significa Valores Separados por Comas (Comma-Separated Values). Es un formato de archivo simple utilizado para almacenar datos tabulares, donde cada línea representa una fila y los valores en cada fila están separados por comas.

Ahora, creemos el archivo `reader.py`. Sigue estos pasos:

1. Abre el editor de código y crea un nuevo archivo llamado `reader.py` en el directorio `/home/labex/project`. Aquí es donde escribiremos nuestras funciones para leer datos de archivos CSV.

2. Agrega el siguiente código a `reader.py`:

```python
# reader.py

import csv

def read_csv_as_dicts(filename, types):
    '''
    Read CSV data into a list of dictionaries with optional type conversion

    Args:
        filename: Path to the CSV file
        types: List of type conversion functions for each column

    Returns:
        List of dictionaries with data from the CSV file
    '''
    records = []
    with open(filename) as file:
        rows = csv.reader(file)
        headers = next(rows)
        for row in rows:
            record = { name: func(val)
                       for name, func, val in zip(headers, types, row) }
            records.append(record)
    return records

def read_csv_as_instances(filename, cls):
    '''
    Read CSV data into a list of class instances

    Args:
        filename: Path to the CSV file
        cls: Class to create instances from

    Returns:
        List of class instances with data from the CSV file
    '''
    records = []
    with open(filename) as file:
        rows = csv.reader(file)
        headers = next(rows)
        for row in rows:
            record = cls.from_row(row)
            records.append(record)
    return records
```

En la función `read_csv_as_dicts`, primero abrimos el archivo CSV utilizando la función `open`. Luego, usamos `csv.reader` para leer el archivo línea por línea. La declaración `next(rows)` lee la primera línea del archivo, que generalmente contiene los encabezados. Después de eso, iteramos sobre las filas restantes. Para cada fila, creamos un diccionario donde las claves son los encabezados y los valores son los valores correspondientes en la fila, con una conversión de tipo opcional utilizando la lista `types`.

La función `read_csv_as_instances` es similar, pero en lugar de crear diccionarios, crea instancias de una clase dada. Asume que la clase tiene un método estático llamado `from_row` que puede crear una instancia a partir de una fila de datos.

3. Probemos estas funciones para asegurarnos de que funcionen correctamente. Crea un nuevo archivo llamado `test_reader.py` con el siguiente código:

```python
# test_reader.py

import reader
import stock

# Test reading CSV as dictionaries
portfolio_dicts = reader.read_csv_as_dicts('portfolio.csv', [str, int, float])
print("First portfolio item as dictionary:", portfolio_dicts[0])
print("Total items:", len(portfolio_dicts))

# Test reading CSV as class instances
portfolio_instances = reader.read_csv_as_instances('portfolio.csv', stock.Stock)
print("\nFirst portfolio item as Stock instance:", portfolio_instances[0])
print("Total items:", len(portfolio_instances))
```

En el archivo `test_reader.py`, importamos el módulo `reader` que acabamos de crear y el módulo `stock`. Luego probamos las dos funciones llamándolas con un archivo CSV de muestra llamado `portfolio.csv`. Imprimimos el primer elemento y el número total de elementos en la cartera para verificar que las funciones funcionen como se espera.

4. Ejecuta el script de prueba desde la terminal:

```bash
python test_reader.py
```

La salida debería ser similar a esta:

```
First portfolio item as dictionary: {'name': 'AA', 'shares': 100, 'price': 32.2}
Total items: 7

First portfolio item as Stock instance: Stock('AA', 100, 32.2)
Total items: 7
```

Esto confirma que nuestras dos funciones funcionan correctamente. La primera función convierte los datos de un archivo CSV en una lista de diccionarios con una conversión de tipo adecuada, y la segunda función crea instancias de clase utilizando un método estático en la clase proporcionada.

En el siguiente paso, refactorizaremos estas funciones para hacerlas más flexibles permitiéndoles trabajar con cualquier fuente iterable de datos, no solo con nombres de archivos.
