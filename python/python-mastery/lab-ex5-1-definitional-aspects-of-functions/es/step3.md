# Haciendo las funciones más flexibles

Actualmente, nuestras funciones se limitan a leer desde archivos especificados por un nombre de archivo. Esto restringe su usabilidad. En programación, a menudo es beneficioso hacer que las funciones sean más flexibles para que puedan manejar diferentes tipos de entrada. En nuestro caso, sería genial si nuestras funciones pudieran trabajar con cualquier iterable que produzca líneas, como objetos de archivo u otras fuentes. De esta manera, podemos usar estas funciones en más escenarios, como leer desde archivos comprimidos u otros flujos de datos.

Refactoricemos nuestro código para habilitar esta flexibilidad:

1. Abre el archivo `reader.py`. Lo vamos a modificar para incluir algunas nuevas funciones. Estas nuevas funciones permitirán que nuestro código funcione con diferentes tipos de iterables. Aquí está el código que debes agregar:

```python
# reader.py

import csv

def csv_as_dicts(lines, types):
    '''
    Parse CSV data from an iterable into a list of dictionaries

    Args:
        lines: An iterable producing CSV lines
        types: List of type conversion functions for each column

    Returns:
        List of dictionaries with data from the CSV lines
    '''
    records = []
    rows = csv.reader(lines)
    headers = next(rows)
    for row in rows:
        record = { name: func(val)
                  for name, func, val in zip(headers, types, row) }
        records.append(record)
    return records

def csv_as_instances(lines, cls):
    '''
    Parse CSV data from an iterable into a list of class instances

    Args:
        lines: An iterable producing CSV lines
        cls: Class to create instances from

    Returns:
        List of class instances with data from the CSV lines
    '''
    records = []
    rows = csv.reader(lines)
    headers = next(rows)
    for row in rows:
        record = cls.from_row(row)
        records.append(record)
    return records

def read_csv_as_dicts(filename, types):
    '''
    Read CSV data into a list of dictionaries with optional type conversion

    Args:
        filename: Path to the CSV file
        types: List of type conversion functions for each column

    Returns:
        List of dictionaries with data from the CSV file
    '''
    with open(filename) as file:
        return csv_as_dicts(file, types)

def read_csv_as_instances(filename, cls):
    '''
    Read CSV data into a list of class instances

    Args:
        filename: Path to the CSV file
        cls: Class to create instances from

    Returns:
        List of class instances with data from the CSV file
    '''
    with open(filename) as file:
        return csv_as_instances(file, cls)
```

Veamos de cerca cómo hemos refactorizado el código:

1. Hemos creado dos funciones más genéricas, `csv_as_dicts()` y `csv_as_instances()`. Estas funciones están diseñadas para trabajar con cualquier iterable que produzca líneas de CSV. Esto significa que pueden manejar diferentes tipos de fuentes de entrada, no solo archivos especificados por un nombre de archivo.
2. Hemos reimplementado `read_csv_as_dicts()` y `read_csv_as_instances()` para usar estas nuevas funciones. De esta manera, la funcionalidad original de leer desde un archivo por nombre de archivo sigue estando disponible, pero ahora se basa en las funciones más flexibles.
3. Este enfoque mantiene la compatibilidad hacia atrás con el código existente. Eso significa que cualquier código que estaba usando las funciones antiguas seguirá funcionando como se espera. Al mismo tiempo, nuestra biblioteca se vuelve más flexible porque ahora puede manejar diferentes tipos de fuentes de entrada.

4. Ahora, probemos estas nuevas funciones. Crea un archivo llamado `test_reader_flexibility.py` y agrega el siguiente código a él. Este código probará las nuevas funciones con diferentes tipos de fuentes de entrada:

```python
# test_reader_flexibility.py

import reader
import stock
import gzip

# Test opening a regular file
with open('portfolio.csv') as file:
    portfolio = reader.csv_as_dicts(file, [str, int, float])
    print("First item from open file:", portfolio[0])

# Test opening a gzipped file
with gzip.open('portfolio.csv.gz', 'rt') as file:  # 'rt' means read text
    portfolio = reader.csv_as_instances(file, stock.Stock)
    print("\nFirst item from gzipped file:", portfolio[0])

# Test backward compatibility
portfolio = reader.read_csv_as_dicts('portfolio.csv', [str, int, float])
print("\nFirst item using backward compatible function:", portfolio[0])
```

3. Después de crear el archivo de prueba, necesitamos ejecutar el script de prueba desde la terminal. Abre tu terminal y navega hasta el directorio donde se encuentra el archivo `test_reader_flexibility.py`. Luego ejecuta el siguiente comando:

```bash
python test_reader_flexibility.py
```

La salida debería ser similar a esta:

```
First item from open file: {'name': 'AA', 'shares': 100, 'price': 32.2}

First item from gzipped file: Stock('AA', 100, 32.2)

First item using backward compatible function: {'name': 'AA', 'shares': 100, 'price': 32.2}
```

Esta salida confirma que nuestras funciones ahora funcionan con diferentes tipos de fuentes de entrada mientras mantienen la compatibilidad hacia atrás. Las funciones refactorizadas pueden procesar datos de:

- Archivos regulares abiertos con `open()`
- Archivos comprimidos abiertos con `gzip.open()`
- Cualquier otro objeto iterable que produzca líneas de texto

Esto hace que nuestro código sea mucho más flexible y fácil de usar en diferentes escenarios.
