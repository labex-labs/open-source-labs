# Optimización de la memoria con datos orientados a columnas

En el almacenamiento de datos tradicional, a menudo almacenamos cada registro como un diccionario separado, lo que se conoce como enfoque orientado a filas (row-oriented approach). Sin embargo, este método puede consumir una cantidad significativa de memoria. Una forma alternativa es almacenar los datos en columnas. En el enfoque orientado a columnas, creamos listas separadas para cada atributo, y cada lista contiene todos los valores de ese atributo específico. Esto puede ayudarnos a ahorrar memoria.

1. Primero, necesitas crear un nuevo archivo de Python en el directorio de tu proyecto. Este archivo contendrá el código para leer datos de manera orientada a columnas. Nombrar el archivo `readrides.py`. Puedes usar los siguientes comandos en la terminal para lograr esto:

```bash
cd ~/project
touch readrides.py
```

El comando `cd ~/project` cambia el directorio actual al directorio de tu proyecto, y el comando `touch readrides.py` crea un nuevo archivo vacío llamado `readrides.py`.

2. A continuación, abre el archivo `readrides.py` en el editor WebIDE. Luego, agrega el siguiente código de Python al archivo. Este código define una función `read_rides_as_columns` que lee los datos de viajes en autobús desde un archivo CSV y los almacena en cuatro listas separadas, cada una representando una columna de datos.

```python
# readrides.py
import csv
import sys
import tracemalloc

def read_rides_as_columns(filename):
    '''
    Read the bus ride data into 4 lists, representing columns
    '''
    routes = []
    dates = []
    daytypes = []
    numrides = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)     # Skip headers
        for row in rows:
            routes.append(row[0])
            dates.append(row[1])
            daytypes.append(row[2])
            numrides.append(int(row[3]))
    return dict(routes=routes, dates=dates, daytypes=daytypes, numrides=numrides)
```

En este código, primero importamos los módulos necesarios `csv`, `sys` y `tracemalloc`. El módulo `csv` se utiliza para leer archivos CSV, `sys` se puede utilizar para operaciones relacionadas con el sistema (aunque no se utiliza en esta función), y `tracemalloc` se utiliza para el análisis de memoria. Dentro de la función, inicializamos cuatro listas vacías para almacenar diferentes columnas de datos. Luego, abrimos el archivo, omitimos la fila de encabezados y recorremos cada fila del archivo, anexando los valores correspondientes a las listas adecuadas. Finalmente, devolvemos un diccionario que contiene estas cuatro listas.

3. Ahora, analicemos por qué el enfoque orientado a columnas puede ahorrar memoria. Lo haremos en la shell de Python. Ejecuta el siguiente código:

```python
import readrides
import tracemalloc

# Estimate memory for row-oriented approach
nrows = 577563     # Number of rows in original file
dict_overhead = 240  # Approximate dictionary overhead in bytes
row_memory = nrows * dict_overhead
print(f"Estimated memory for row-oriented data: {row_memory} bytes ({row_memory/1024/1024:.2f} MB)")

# Estimate memory for column-oriented approach
pointer_size = 8   # Size of a pointer in bytes on 64-bit systems
column_memory = nrows * 4 * pointer_size  # 4 columns with one pointer per entry
print(f"Estimated memory for column-oriented data: {column_memory} bytes ({column_memory/1024/1024:.2f} MB)")

# Estimate savings
savings = row_memory - column_memory
print(f"Estimated memory savings: {savings} bytes ({savings/1024/1024:.2f} MB)")
```

En este código, primero importamos el módulo `readrides` que acabamos de crear y el módulo `tracemalloc`. Luego, estimamos el uso de memoria para el enfoque orientado a filas. Asumimos que cada diccionario tiene una sobrecarga de 240 bytes, y multiplicamos esto por el número de filas en el archivo original para obtener el uso total de memoria para los datos orientados a filas. Para el enfoque orientado a columnas, asumimos que en un sistema de 64 bits, cada puntero ocupa 8 bytes. Dado que tenemos 4 columnas y un puntero por entrada, calculamos el uso total de memoria para los datos orientados a columnas. Finalmente, calculamos el ahorro de memoria restando el uso de memoria orientado a columnas del uso de memoria orientado a filas.

Este cálculo muestra que el enfoque orientado a columnas debería ahorrar alrededor de 120 MB de memoria en comparación con el enfoque orientado a filas con diccionarios.

4. Verifiquemos esto midiendo el uso real de memoria con el módulo `tracemalloc`. Ejecuta el siguiente código:

```python
# Start tracking memory
tracemalloc.start()

# Read the data
columns = readrides.read_rides_as_columns('ctabus.csv')

# Get current and peak memory usage
current, peak = tracemalloc.get_traced_memory()
print(f"Current memory usage: {current/1024/1024:.2f} MB")
print(f"Peak memory usage: {peak/1024/1024:.2f} MB")

# Stop tracking memory
tracemalloc.stop()
```

En este código, primero comenzamos a realizar un seguimiento de la memoria utilizando `tracemalloc.start()`. Luego, llamamos a la función `read_rides_as_columns` para leer los datos del archivo `ctabus.csv`. Después, usamos `tracemalloc.get_traced_memory()` para obtener el uso actual y máximo de memoria. Finalmente, detenemos el seguimiento de la memoria utilizando `tracemalloc.stop()`.

La salida mostrará el uso real de memoria de tu estructura de datos orientada a columnas. Esto debería ser significativamente menor que nuestra estimación teórica para el enfoque orientado a filas.

El importante ahorro de memoria proviene de eliminar la sobrecarga de miles de objetos de diccionario. Cada diccionario en Python tiene una sobrecarga fija independientemente de cuántos elementos contenga. Al utilizar un almacenamiento orientado a columnas, solo necesitamos unas pocas listas en lugar de miles de diccionarios.
