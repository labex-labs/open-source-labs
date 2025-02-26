# Ejercicio 8.2: Agregar registro a un módulo

En `fileparse.py`, hay un manejo de errores relacionado con las excepciones causadas por entradas incorrectas. Se ve así:

```python
# fileparse.py
import csv

def parse_csv(lines, select=None, types=None, has_headers=True, delimiter=',', silence_errors=False):
    '''
    Analiza un archivo CSV en una lista de registros con conversión de tipo.
    '''
    if select and not has_headers:
        raise RuntimeError('select requiere encabezados de columna')

    rows = csv.reader(lines, delimiter=delimiter)

    # Lee los encabezados del archivo (si los hay)
    headers = next(rows) if has_headers else []

    # Si se han seleccionado columnas específicas, crea índices para filtrado y establece columnas de salida
    if select:
        indices = [ headers.index(colname) for colname in select ]
        headers = select

    records = []
    for rowno, row in enumerate(rows, 1):
        if not row:     # Omite filas sin datos
            continue

        # Si se seleccionan índices de columna específicos, escoge ellos
        if select:
            row = [ row[index] for index in indices]

        # Aplica la conversión de tipo a la fila
        if types:
            try:
                row = [func(val) for func, val in zip(types, row)]
            except ValueError as e:
                if not silence_errors:
                    print(f"Fila {rowno}: No se pudo convertir {row}")
                    print(f"Fila {rowno}: Razón {e}")
                continue

        # Crea un diccionario o una tupla
        if headers:
            record = dict(zip(headers, row))
        else:
            record = tuple(row)
        records.append(record)

    return records
```

Observa las declaraciones `print` que emiten mensajes de diagnóstico. Reemplazar esas impresiones con operaciones de registro es relativamente sencillo. Cambia el código de la siguiente manera:

```python
# fileparse.py
import csv
import logging
log = logging.getLogger(__name__)

def parse_csv(lines, select=None, types=None, has_headers=True, delimiter=',', silence_errors=False):
    '''
    Analiza un archivo CSV en una lista de registros con conversión de tipo.
    '''
    if select and not has_headers:
        raise RuntimeError('select requiere encabezados de columna')

    rows = csv.reader(lines, delimiter=delimiter)

    # Lee los encabezados del archivo (si los hay)
    headers = next(rows) if has_headers else []

    # Si se han seleccionado columnas específicas, crea índices para filtrado y establece columnas de salida
    if select:
        indices = [ headers.index(colname) for colname in select ]
        headers = select

    records = []
    for rowno, row in enumerate(rows, 1):
        if not row:     # Omite filas sin datos
            continue

        # Si se seleccionan índices de columna específicos, escoge ellos
        if select:
            row = [ row[index] for index in indices]

        # Aplica la conversión de tipo a la fila
        if types:
            try:
                row = [func(val) for func, val in zip(types, row)]
            except ValueError as e:
                if not silence_errors:
                    log.warning("Fila %d: No se pudo convertir %s", rowno, row)
                    log.debug("Fila %d: Razón %s", rowno, e)
                continue

        # Crea un diccionario o una tupla
        if headers:
            record = dict(zip(headers, row))
        else:
            record = tuple(row)
        records.append(record)

    return records
```

Ahora que has hecho estos cambios, intenta usar un poco de tu código con datos incorrectos.

```python
>>> import report
>>> a = report.read_portfolio('missing.csv')
Fila 4: Fila incorrecta: ['MSFT', '', '51.23']
Fila 7: Fila incorrecta: ['IBM', '', '70.44']
>>>
```

Si no haces nada, solo obtendrás mensajes de registro para el nivel `WARNING` y superior. La salida se verá como declaraciones `print` simples. Sin embargo, si configuras el módulo de registro, obtendrás información adicional sobre los niveles de registro, el módulo y más. Escribe estos pasos para ver eso:

```python
>>> import logging
>>> logging.basicConfig()
>>> a = report.read_portfolio('missing.csv')
WARNING:fileparse:Fila 4: Fila incorrecta: ['MSFT', '', '51.23']
WARNING:fileparse:Fila 7: Fila incorrecta: ['IBM', '', '70.44']
>>>
```

Notarás que no ves la salida de la operación `log.debug()`. Escribe esto para cambiar el nivel.

```python
>>> logging.getLogger('fileparse').setLevel(logging.DEBUG)
>>> a = report.read_portfolio('missing.csv')
WARNING:fileparse:Fila 4: Fila incorrecta: ['MSFT', '', '51.23']
DEBUG:fileparse:Fila 4: Razón: literal no válido para int() con base 10: ''
WARNING:fileparse:Fila 7: Fila incorrecta: ['IBM', '', '70.44']
DEBUG:fileparse:Fila 7: Razón: literal no válido para int() con base 10: ''
>>>
```

Desactiva todos, excepto los mensajes de registro más críticos:

```python
>>> logging.getLogger('fileparse').setLevel(logging.CRITICAL)
>>> a = report.read_portfolio('missing.csv')
>>>
```
