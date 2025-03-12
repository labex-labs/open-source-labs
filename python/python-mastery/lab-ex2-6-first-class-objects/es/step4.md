# Almacenamiento de Datos Orientado a Columnas

Hasta ahora, hemos estado almacenando los datos CSV como una lista de diccionarios de filas. Esto significa que cada fila en el archivo CSV se representa como un diccionario, donde las claves son los encabezados de las columnas y los valores son los datos correspondientes en esa fila. Sin embargo, cuando se trabaja con grandes conjuntos de datos, este método puede ser ineficiente. Almacenar los datos en un formato orientado a columnas puede ser una mejor opción. En un enfoque orientado a columnas, los datos de cada columna se almacenan en una lista separada. Esto puede reducir significativamente el uso de memoria porque los tipos de datos similares se agrupan juntos, y también puede mejorar el rendimiento para ciertas operaciones, como la agregación de datos por columna.

## Creando un Lector de Datos Orientado a Columnas

Ahora, vamos a crear un nuevo archivo que nos ayudará a leer los datos CSV en un formato orientado a columnas. Crea un nuevo archivo llamado `colreader.py` en el directorio del proyecto con el siguiente código:

```python
import csv

class DataCollection:
    def __init__(self, headers, columns):
        """
        Initialize a column-oriented data collection.

        Parameters:
        headers (list): Column header names
        columns (dict): Dictionary mapping header names to column data lists
        """
        self.headers = headers
        self.columns = columns
        self._length = len(columns[headers[0]]) if headers else 0

    def __len__(self):
        """Return the number of rows in the collection."""
        return self._length

    def __getitem__(self, index):
        """
        Get a row by index, presented as a dictionary.

        Parameters:
        index (int): Row index

        Returns:
        dict: Dictionary representing the row at the given index
        """
        if isinstance(index, int):
            if index < 0 or index >= self._length:
                raise IndexError("Index out of range")

            return {header: self.columns[header][index] for header in self.headers}
        else:
            raise TypeError("Index must be an integer")

def read_csv_as_columns(filename, types):
    """
    Read a CSV file into a column-oriented data structure, converting each field
    according to the types provided.

    Parameters:
    filename (str): Name of the CSV file to read
    types (list): List of type conversion functions for each column

    Returns:
    DataCollection: Column-oriented data collection representing the CSV data
    """
    with open(filename, 'r') as f:
        rows = csv.reader(f)
        headers = next(rows)  # Get the column headers

        # Initialize columns
        columns = {header: [] for header in headers}

        # Read data into columns
        for row in rows:
            # Convert values according to the specified types
            converted_values = [func(val) for func, val in zip(types, row)]

            # Add each value to its corresponding column
            for header, value in zip(headers, converted_values):
                columns[header].append(value)

    return DataCollection(headers, columns)
```

Este código hace dos cosas importantes:

1. Define una clase `DataCollection`. Esta clase almacena los datos en columnas, pero nos permite acceder a los datos como si fuera una lista de diccionarios de filas. Esto es útil porque proporciona una forma familiar de trabajar con los datos.
2. Define una función `read_csv_as_columns`. Esta función lee los datos CSV de un archivo y los almacena en una estructura orientada a columnas. También convierte cada campo en el archivo CSV de acuerdo con los tipos que proporcionamos.

## Probando el Lector Orientado a Columnas

Probemos nuestro lector orientado a columnas utilizando los datos de autobuses del CTA. Primero, abre un intérprete de Python. Puedes hacer esto ejecutando el siguiente comando en tu terminal:

```bash
python3
```

Una vez que el intérprete de Python esté abierto, ejecuta el siguiente código:

```python
import colreader
import tracemalloc
from sys import intern

# Start memory tracking
tracemalloc.start()

# Read data into column-oriented structure with string interning
data = colreader.read_csv_as_columns('ctabus.csv', [intern, intern, intern, int])

# Check that we can access the data like a list of dictionaries
print(f"Number of rows: {len(data)}")
print("First 3 rows:")
for i in range(3):
    print(data[i])

# Check memory usage
current, peak = tracemalloc.get_traced_memory()
print(f"Current memory usage: {current / 1024 / 1024:.2f} MB")
print(f"Peak memory usage: {peak / 1024 / 1024:.2f} MB")
```

La salida debería ser así:

```
Number of rows: 577563
First 3 rows:
{'route': '3', 'date': '01/01/2001', 'daytype': 'U', 'rides': 7354}
{'route': '4', 'date': '01/01/2001', 'daytype': 'U', 'rides': 9288}
{'route': '6', 'date': '01/01/2001', 'daytype': 'U', 'rides': 6048}
Current memory usage: 38.67 MB
Peak memory usage: 103.42 MB
```

Ahora, comparemos esto con nuestro enfoque anterior orientado a filas. Ejecuta el siguiente código en el mismo intérprete de Python:

```python
import reader
import tracemalloc
from sys import intern

# Reset memory tracking
tracemalloc.reset_peak()

# Read data into row-oriented structure with string interning
rows = reader.read_csv_as_dicts('ctabus.csv', [intern, intern, intern, int])

# Check memory usage
current, peak = tracemalloc.get_traced_memory()
print(f"Current memory usage (row-oriented): {current / 1024 / 1024:.2f} MB")
print(f"Peak memory usage (row-oriented): {peak / 1024 / 1024:.2f} MB")
```

La salida debería ser algo como esto:

```
Current memory usage (row-oriented): 170.23 MB
Peak memory usage (row-oriented): 190.05 MB
```

Como se puede ver, el enfoque orientado a columnas utiliza significativamente menos memoria.

Probemos también que todavía podemos analizar los datos como antes. Ejecuta el siguiente código:

```python
# Find all unique routes in the column-oriented data
routes = {row['route'] for row in data}
print(f"Number of unique routes: {len(routes)}")

# Count rides per route (first 5)
from collections import defaultdict
route_rides = defaultdict(int)
for row in data:
    route_rides[row['route']] += row['rides']

# Show the top 5 routes by total rides
top_routes = sorted(route_rides.items(), key=lambda x: x[1], reverse=True)[:5]
print("Top 5 routes by total rides:")
for route, rides in top_routes:
    print(f"Route {route}: {rides:,} rides")
```

La salida debería ser:

```
Number of unique routes: 181
Top 5 routes by total rides:
Route 9: 158,545,826 rides
Route 49: 129,872,910 rides
Route 77: 120,086,065 rides
Route 79: 109,348,708 rides
Route 4: 91,405,538 rides
```

Finalmente, sal del intérprete de Python ejecutando el siguiente comando:

```python
exit()
```

Podemos ver que el enfoque orientado a columnas no solo ahorra memoria, sino que también nos permite realizar los mismos análisis que antes. Esto muestra cómo diferentes estrategias de almacenamiento de datos pueden tener un impacto significativo en el rendimiento mientras todavía proporcionan la misma interfaz para trabajar con los datos.
