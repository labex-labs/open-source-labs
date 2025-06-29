# Comparación de diferentes estructuras de datos

En Python, las estructuras de datos se utilizan para organizar y almacenar datos relacionados. Son como contenedores que guardan diferentes tipos de información de manera estructurada. En este paso, compararemos diferentes estructuras de datos y veremos cuánta memoria utilizan.

Vamos a crear un nuevo archivo llamado `compare_structures.py` en el directorio `/home/labex/project`. Este archivo contendrá el código para leer datos de un archivo CSV y almacenarlos en diferentes estructuras de datos.

```python
# compare_structures.py
import csv
import tracemalloc
from collections import namedtuple

# Define a named tuple for rides data
RideRecord = namedtuple('RideRecord', ['route', 'date', 'daytype', 'rides'])

# A named tuple is a lightweight class that allows you to access its fields by name.
# It's like a tuple, but with named attributes.

# Define a class with __slots__ for memory optimization
class SlottedRideRecord:
    __slots__ = ['route', 'date', 'daytype', 'rides']

    def __init__(self, route, date, daytype, rides):
        self.route = route
        self.date = date
        self.daytype = daytype
        self.rides = rides

# A class with __slots__ is a memory - optimized class.
# It avoids using an instance dictionary, which saves memory.

# Define a regular class for rides data
class RegularRideRecord:
    def __init__(self, route, date, daytype, rides):
        self.route = route
        self.date = date
        self.daytype = daytype
        self.rides = rides

# A regular class is an object - oriented way to represent data.
# It has named attributes and can have methods.

# Function to read data as tuples
def read_as_tuples(filename):
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        next(rows)  # Skip headers
        for row in rows:
            record = (row[0], row[1], row[2], int(row[3]))
            records.append(record)
    return records

# This function reads data from a CSV file and stores it as tuples.
# Tuples are immutable sequences, and you access their elements by numeric index.

# Function to read data as dictionaries
def read_as_dicts(filename):
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)  # Get headers
        for row in rows:
            record = {
                'route': row[0],
                'date': row[1],
                'daytype': row[2],
                'rides': int(row[3])
            }
            records.append(record)
    return records

# This function reads data from a CSV file and stores it as dictionaries.
# Dictionaries use key - value pairs, so you can access elements by their names.

# Function to read data as named tuples
def read_as_named_tuples(filename):
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        next(rows)  # Skip headers
        for row in rows:
            record = RideRecord(row[0], row[1], row[2], int(row[3]))
            records.append(record)
    return records

# This function reads data from a CSV file and stores it as named tuples.
# Named tuples combine the efficiency of tuples with the readability of named access.

# Function to read data as regular class instances
def read_as_regular_classes(filename):
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        next(rows)  # Skip headers
        for row in rows:
            record = RegularRideRecord(row[0], row[1], row[2], int(row[3]))
            records.append(record)
    return records

# This function reads data from a CSV file and stores it as instances of a regular class.
# Regular classes allow you to add methods to your data.

# Function to read data as slotted class instances
def read_as_slotted_classes(filename):
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        next(rows)  # Skip headers
        for row in rows:
            record = SlottedRideRecord(row[0], row[1], row[2], int(row[3]))
            records.append(record)
    return records

# This function reads data from a CSV file and stores it as instances of a slotted class.
# Slotted classes are memory - optimized and still provide named access.

# Function to measure memory usage
def measure_memory(func, filename):
    tracemalloc.start()

    records = func(filename)

    current, peak = tracemalloc.get_traced_memory()

    # Demonstrate how to use each data structure
    first_record = records[0]
    if func.__name__ == 'read_as_tuples':
        route, date, daytype, rides = first_record
    elif func.__name__ == 'read_as_dicts':
        route = first_record['route']
        date = first_record['date']
        daytype = first_record['daytype']
        rides = first_record['rides']
    else:  # named tuples and classes
        route = first_record.route
        date = first_record.date
        daytype = first_record.daytype
        rides = first_record.rides

    print(f"Structure type: {func.__name__}")
    print(f"Record count: {len(records)}")
    print(f"Example access: Route={route}, Date={date}, Rides={rides}")
    print(f"Current memory: {current/1024/1024:.2f} MB")
    print(f"Peak memory: {peak/1024/1024:.2f} MB")
    print("-" * 50)

    tracemalloc.stop()

    return current

if __name__ == "__main__":
    filename = '/home/labex/project/ctabus.csv'

    # Run all memory tests
    print("Memory usage comparison for different data structures:\n")

    results = []
    for reader_func in [
        read_as_tuples,
        read_as_dicts,
        read_as_named_tuples,
        read_as_regular_classes,
        read_as_slotted_classes
    ]:
        memory = measure_memory(reader_func, filename)
        results.append((reader_func.__name__, memory))

    # Sort by memory usage (lowest first)
    results.sort(key=lambda x: x[1])

    print("\nRanking by memory efficiency (most efficient first):")
    for i, (name, memory) in enumerate(results, 1):
        print(f"{i}. {name}: {memory/1024/1024:.2f} MB")
```

Ejecuta el script para ver los resultados de la comparación:

```bash
python3 /home/labex/project/compare_structures.py
```

La salida mostrará el uso de memoria de cada estructura de datos, junto con un ranking de la más a la menos eficiente en términos de memoria.

## Comprendiendo las diferentes estructuras de datos

1. **Tuplas**:
   - Las tuplas son secuencias ligeras e inmutables. Esto significa que una vez que creas una tupla, no puedes cambiar sus elementos.
   - Accedes a los elementos de una tupla por su índice numérico, como `record[0]`, `record[1]`, etc.
   - Son muy eficientes en términos de memoria porque tienen una estructura simple.
   - Sin embargo, pueden ser menos legibles porque necesitas recordar el índice de cada elemento.

2. **Diccionarios**:
   - Los diccionarios utilizan pares clave - valor, lo que te permite acceder a los elementos por sus nombres.
   - Son más legibles, por ejemplo, puedes usar `record['route']`, `record['date']`, etc.
   - Tienen un mayor uso de memoria debido al gasto de la tabla hash utilizada para almacenar los pares clave - valor.
   - Son flexibles porque puedes agregar o eliminar campos fácilmente.

3. **Tuplas con nombres (Named Tuples)**:
   - Las tuplas con nombres combinan la eficiencia de las tuplas con la capacidad de acceder a los elementos por nombre.
   - Puedes acceder a los elementos usando la notación de punto, como `record.route`, `record.date`, etc.
   - Son inmutables, al igual que las tuplas normales.
   - Son más eficientes en términos de memoria que los diccionarios.

4. **Clases regulares**:
   - Las clases regulares siguen un enfoque orientado a objetos y tienen atributos con nombre.
   - Puedes acceder a los atributos usando la notación de punto, como `record.route`, `record.date`, etc.
   - Puedes agregar métodos a una clase regular para definir comportamiento.
   - Utilizan más memoria porque cada instancia tiene un diccionario de instancia para almacenar sus atributos.

5. **Clases con `__slots__`**:
   - Las clases con `__slots__` son clases optimizadas en términos de memoria. Evitan usar un diccionario de instancia, lo que ahorra memoria.
   - Todavía proporcionan acceso con nombre a los atributos, como `record.route`, `record.date`, etc.
   - Restringen la adición de nuevos atributos después de que se crea el objeto.
   - Son más eficientes en términos de memoria que las clases regulares.

## Cuándo usar cada enfoque

- **Tuplas**: Utiliza tuplas cuando la memoria sea un factor crítico y solo necesites un acceso indexado simple a tus datos.
- **Diccionarios**: Utiliza diccionarios cuando necesites flexibilidad, como cuando los campos de tus datos pueden variar.
- **Tuplas con nombres (Named Tuples)**: Utiliza tuplas con nombres cuando necesites legibilidad y eficiencia en términos de memoria.
- **Clases regulares**: Utiliza clases regulares cuando necesites agregar comportamiento (métodos) a tus datos.
- **Clases con `__slots__`**: Utiliza clases con `__slots__` cuando necesites comportamiento y máxima eficiencia en términos de memoria.

Al elegir la estructura de datos adecuada para tus necesidades, puedes mejorar significativamente el rendimiento y el uso de memoria de tus programas de Python, especialmente cuando trabajes con grandes conjuntos de datos.
