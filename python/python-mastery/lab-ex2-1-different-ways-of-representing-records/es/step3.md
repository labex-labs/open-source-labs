# Una Lista de Tuplas

En la práctica, es posible que lea los datos en una lista y convierta cada línea en alguna otra estructura de datos. Aquí hay un programa `readrides.py` que lee todo el archivo en una lista de tuplas utilizando el módulo `csv`:

```python
# readrides.py

import csv

def read_rides_as_tuples(filename):
    '''
    Lee los datos de viajes de autobús como una lista de tuplas
    '''
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)     # Omite los encabezados
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = (route, date, daytype, rides)
            records.append(record)
    return records

if __name__ == '__main__':
    import tracemalloc
    tracemalloc.start()
    rows = read_rides_as_tuples('/home/labex/project/ctabus.csv')
    print('Memory Use: Current %d, Peak %d' % tracemalloc.get_traced_memory())
```

Ejecute este programa usando `python3 -i readrides.py` y examine el contenido resultante de `rows`. Debería obtener una lista de tuplas como esta:

```python
>>> len(rows)
577563
>>> rows[0]
('3', '01/01/2001', 'U', 7354)
>>> rows[1]
('4', '01/01/2001', 'U', 9288)
```

Examine el uso de memoria resultante. Debería ser sustancialmente mayor que en el paso 2.
