# Trabajando con datos estructurados usando tuplas

Hasta ahora, hemos estado trabajando con el almacenamiento de datos de texto sin procesar. Pero cuando se trata de análisis de datos, generalmente necesitamos transformar los datos en formatos más organizados y estructurados. Esto facilita la realización de diversas operaciones y la obtención de información a partir de los datos. En este paso, aprenderemos cómo leer datos como una lista de tuplas utilizando el módulo `csv`. Las tuplas son una estructura de datos simple y útil en Python que puede contener múltiples valores.

## Creando una función lectora con tuplas

Vamos a crear un nuevo archivo llamado `readrides.py` en el directorio `/home/labex/project`. Este archivo contendrá el código para leer los datos de un archivo CSV y almacenarlos como una lista de tuplas.

```python
# readrides.py
import csv
import tracemalloc

def read_rides_as_tuples(filename):
    '''
    Read the bus ride data as a list of tuples
    '''
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)     # Skip headers
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = (route, date, daytype, rides)
            records.append(record)
    return records

if __name__ == '__main__':
    tracemalloc.start()

    rows = read_rides_as_tuples('/home/labex/project/ctabus.csv')

    current, peak = tracemalloc.get_traced_memory()
    print(f'Number of records: {len(rows)}')
    print(f'First record: {rows[0]}')
    print(f'Second record: {rows[1]}')
    print(f'Memory Use: Current {current/1024/1024:.2f} MB, Peak {peak/1024/1024:.2f} MB')
```

Este script define una función llamada `read_rides_as_tuples`. Esto es lo que hace paso a paso:

1. Abre el archivo CSV especificado por el parámetro `filename`. Esto nos permite acceder a los datos dentro del archivo.
2. Utiliza el módulo `csv` para analizar cada línea del archivo. La función `csv.reader` nos ayuda a dividir las líneas en valores individuales.
3. Extrae los cuatro campos (ruta, fecha, tipo de día y número de viajes) de cada fila. Estos campos son importantes para nuestro análisis de datos.
4. Convierte el campo 'rides' a un entero. Esto es necesario porque los datos en el archivo CSV están inicialmente en formato de cadena, y necesitamos un valor numérico para realizar cálculos.
5. Crea una tupla con estos cuatro valores. Las tuplas son inmutables, lo que significa que sus valores no se pueden cambiar una vez creados.
6. Agrega la tupla a una lista llamada `records`. Esta lista contendrá todos los registros del archivo CSV.

Ahora, vamos a ejecutar el script. Abre tu terminal y escribe el siguiente comando:

```bash
python3 /home/labex/project/readrides.py
```

Deberías ver una salida similar a esta:

```
Number of records: 577563
First record: ('3', '01/01/2001', 'U', 7354)
Second record: ('4', '01/01/2001', 'U', 9288)
Memory Use: Current 89.12 MB, Peak 89.15 MB
```

Observa que el uso de memoria ha aumentado en comparación con nuestros ejemplos anteriores. Hay algunas razones para esto:

1. Ahora estamos almacenando los datos en un formato estructurado (tuplas). Los datos estructurados generalmente requieren más memoria porque tienen una organización definida.
2. Cada valor en la tupla es un objeto de Python separado. Los objetos de Python tienen cierto gasto, lo que contribuye al aumento del uso de memoria.
3. Tenemos una estructura de lista adicional que contiene todas estas tuplas. Las listas también ocupan memoria para almacenar sus elementos.

La ventaja de utilizar este enfoque es que nuestros datos ahora están correctamente estructurados y listos para el análisis. Podemos acceder fácilmente a campos específicos de cada registro por índice. Por ejemplo:

```python
# Example of accessing tuple elements (add this to readrides.py file to try it)
first_record = rows[0]
route = first_record[0]
date = first_record[1]
daytype = first_record[2]
rides = first_record[3]
print(f"Route: {route}, Date: {date}, Day type: {daytype}, Rides: {rides}")
```

Sin embargo, acceder a los datos por índice numérico no siempre es intuitivo. Puede ser difícil recordar a qué campo corresponde cada índice, especialmente cuando se trata de un gran número de campos. En el siguiente paso, exploraremos otras estructuras de datos que pueden hacer que nuestro código sea más legible y mantenible.
