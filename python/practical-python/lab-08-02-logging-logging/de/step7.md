# Übung 8.2: Hinzufügen von Protokollierung zu einem Modul

In `fileparse.py` gibt es einige Fehlerbehandlungen, die mit Ausnahmen aufgrund von schlechtem Input zusammenhängen. Es sieht so aus:

```python
# fileparse.py
import csv

def parse_csv(lines, select=None, types=None, has_headers=True, delimiter=',', silence_errors=False):
    '''
    Parse a CSV file into a list of records with type conversion.
    '''
    if select and not has_headers:
        raise RuntimeError('select requires column headers')

    rows = csv.reader(lines, delimiter=delimiter)

    # Read the file headers (if any)
    headers = next(rows) if has_headers else []

    # If specific columns have been selected, make indices for filtering and set output columns
    if select:
        indices = [ headers.index(colname) for colname in select ]
        headers = select

    records = []
    for rowno, row in enumerate(rows, 1):
        if not row:     # Skip rows with no data
            continue

        # If specific column indices are selected, pick them out
        if select:
            row = [ row[index] for index in indices]

        # Apply type conversion to the row
        if types:
            try:
                row = [func(val) for func, val in zip(types, row)]
            except ValueError as e:
                if not silence_errors:
                    print(f"Row {rowno}: Couldn't convert {row}")
                    print(f"Row {rowno}: Reason {e}")
                continue

        # Make a dictionary or a tuple
        if headers:
            record = dict(zip(headers, row))
        else:
            record = tuple(row)
        records.append(record)

    return records
```

Bemerken Sie die `print`-Anweisungen, die diagnostische Nachrichten ausgeben. Das Ersetzen dieser `print`-Anweisungen durch Protokollierungsoperationen ist relativ einfach. Ändern Sie den Code wie folgt:

```python
# fileparse.py
import csv
import logging
log = logging.getLogger(__name__)

def parse_csv(lines, select=None, types=None, has_headers=True, delimiter=',', silence_errors=False):
    '''
    Parse a CSV file into a list of records with type conversion.
    '''
    if select and not has_headers:
        raise RuntimeError('select requires column headers')

    rows = csv.reader(lines, delimiter=delimiter)

    # Read the file headers (if any)
    headers = next(rows) if has_headers else []

    # If specific columns have been selected, make indices for filtering and set output columns
    if select:
        indices = [ headers.index(colname) for colname in select ]
        headers = select

    records = []
    for rowno, row in enumerate(rows, 1):
        if not row:     # Skip rows with no data
            continue

        # If specific column indices are selected, pick them out
        if select:
            row = [ row[index] for index in indices]

        # Apply type conversion to the row
        if types:
            try:
                row = [func(val) for func, val in zip(types, row)]
            except ValueError as e:
                if not silence_errors:
                    log.warning("Row %d: Couldn't convert %s", rowno, row)
                    log.debug("Row %d: Reason %s", rowno, e)
                continue

        # Make a dictionary or a tuple
        if headers:
            record = dict(zip(headers, row))
        else:
            record = tuple(row)
        records.append(record)

    return records
```

Jetzt, nachdem Sie diese Änderungen vorgenommen haben, versuchen Sie, einige Ihres Codes mit schlechtem Daten zu verwenden.

```python
>>> import report
>>> a = report.read_portfolio('missing.csv')
Row 4: Bad row: ['MSFT', '', '51.23']
Row 7: Bad row: ['IBM', '', '70.44']
>>>
```

Wenn Sie nichts tun, erhalten Sie nur Protokollierungsnachrichten für das `WARNING`-Level und darüber. Die Ausgabe wird wie einfache `print`-Anweisungen aussehen. Wenn Sie jedoch das Protokollierungsmodul konfigurieren, erhalten Sie zusätzliche Informationen über die Protokollierungsebenen, das Modul und mehr. Tippen Sie diese Schritte, um das zu sehen:

```python
>>> import logging
>>> logging.basicConfig()
>>> a = report.read_portfolio('missing.csv')
WARNING:fileparse:Row 4: Bad row: ['MSFT', '', '51.23']
WARNING:fileparse:Row 7: Bad row: ['IBM', '', '70.44']
>>>
```

Sie werden bemerken, dass Sie die Ausgabe der `log.debug()`-Operation nicht sehen. Tippen Sie dies, um das Level zu ändern.

```python
>>> logging.getLogger('fileparse').setLevel(logging.DEBUG)
>>> a = report.read_portfolio('missing.csv')
WARNING:fileparse:Row 4: Bad row: ['MSFT', '', '51.23']
DEBUG:fileparse:Row 4: Reason: invalid literal for int() with base 10: ''
WARNING:fileparse:Row 7: Bad row: ['IBM', '', '70.44']
DEBUG:fileparse:Row 7: Reason: invalid literal for int() with base 10: ''
>>>
```

Schalten Sie alle, außer die kritischsten Protokollierungsnachrichten, aus:

```python
>>> logging.getLogger('fileparse').setLevel(logging.CRITICAL)
>>> a = report.read_portfolio('missing.csv')
>>>
```
