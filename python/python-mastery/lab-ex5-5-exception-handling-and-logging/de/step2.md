# Implementierung der Ausnahmebehandlung (Exception Handling)

In diesem Schritt werden wir uns darauf konzentrieren, Ihren Code robuster zu machen. Wenn ein Programm fehlerhafte Daten erhält, stürzt es oft ab. Wir können jedoch eine Technik namens Ausnahmebehandlung (Exception Handling) verwenden, um diese Probleme elegant zu bewältigen. Sie werden die Datei `reader.py` ändern, um dies zu implementieren. Die Ausnahmebehandlung ermöglicht es Ihrem Programm, auch bei unerwarteten Daten weiterlaufen zu können, anstatt abrupt zu stoppen.

## Grundlagen zu Try-Except-Blöcken

Python bietet eine leistungsstarke Möglichkeit, Ausnahmen mit Try-Except-Blöcken zu behandeln. Lassen Sie uns untersuchen, wie diese funktionieren.

```python
try:
    # Code that might cause an exception
    result = risky_operation()
except SomeExceptionType as e:
    # Code that runs if the exception occurs
    handle_exception(e)
```

Im `try`-Block platzieren Sie den Code, der möglicherweise eine Ausnahme auslöst. Eine Ausnahme ist ein Fehler, der während der Ausführung eines Programms auftritt. Wenn Sie beispielsweise versuchen, eine Zahl durch Null zu teilen, wird Python eine `ZeroDivisionError`-Ausnahme auslösen. Wenn in einem `try`-Block eine Ausnahme auftritt, bricht Python die Ausführung des Codes im `try`-Block ab und springt zum passenden `except`-Block. Der `except`-Block enthält den Code, der die Ausnahme behandelt. `SomeExceptionType` ist der Typ der Ausnahme, die Sie abfangen möchten. Sie können bestimmte Typen von Ausnahmen abfangen oder einen allgemeinen `Exception`-Typ verwenden, um alle Arten von Ausnahmen abzufangen. Der Teil `as e` ermöglicht Ihnen den Zugriff auf das Ausnahmeobjekt, das Informationen über den Fehler enthält.

## Änderung des Codes

Jetzt wenden wir das, was wir über Try-Except-Blöcke gelernt haben, auf die Funktion `convert_csv()` an. Öffnen Sie die Datei `reader.py` in Ihrem Editor.

1. Ersetzen Sie die aktuelle `convert_csv()`-Funktion durch den folgenden Code:

```python
def convert_csv(rows, converter, header=True):
    """
    Convert a sequence of rows to an output sequence according to a conversion function.
    """
    if header:
        headers = next(rows)
    else:
        headers = []

    result = []
    for row_idx, row in enumerate(rows, start=1):
        try:
            # Try to convert the row
            result.append(converter(headers, row))
        except Exception as e:
            # Print a warning message for bad rows
            print(f"Row {row_idx}: Bad row: {row}")
            continue

    return result
```

In dieser neuen Implementierung:

- Wir verwenden eine `for`-Schleife anstelle von `map()`, um jede Zeile zu verarbeiten. Dies gibt uns mehr Kontrolle über die Verarbeitung jeder einzelnen Zeile.
- Wir umschließen den Konvertierungscode in einen Try-Except-Block. Dies bedeutet, dass wenn während der Konvertierung einer Zeile eine Ausnahme auftritt, das Programm nicht abstürzt. Stattdessen springt es zum `except`-Block.
- Im `except`-Block geben wir eine Fehlermeldung für ungültige Zeilen aus. Dies hilft uns, zu identifizieren, welche Zeilen Probleme haben.
- Nach dem Ausgeben der Fehlermeldung verwenden wir die `continue`-Anweisung, um die aktuelle Zeile zu überspringen und die Verarbeitung der verbleibenden Zeilen fortzusetzen.

Speichern Sie die Datei nach diesen Änderungen.

## Testen Ihrer Änderungen

Testen wir Ihren geänderten Code mit der Datei `missing.csv`. Öffnen Sie zunächst den Python-Interpreter, indem Sie den folgenden Befehl in Ihrem Terminal ausführen:

```bash
python3
```

Sobald Sie sich im Python-Interpreter befinden, führen Sie den folgenden Code aus:

```python
from reader import read_csv_as_dicts
port = read_csv_as_dicts('missing.csv', types=[str, int, float])
print(f"Number of valid rows processed: {len(port)}")
```

Wenn Sie diesen Code ausführen, sollten Sie Fehlermeldungen für jede problematische Zeile sehen. Das Programm wird jedoch die Verarbeitung fortsetzen und die gültigen Zeilen zurückgeben. Hier ist ein Beispiel für die Ausgabe:

```
Row 4: Bad row: ['C', '', '53.08']
Row 7: Bad row: ['DIS', '50', 'N/A']
Row 8: Bad row: ['GE', '', '37.23']
Row 13: Bad row: ['INTC', '', '21.84']
Row 17: Bad row: ['MCD', '', '51.11']
Row 19: Bad row: ['MO', '', '70.09']
Row 22: Bad row: ['PFE', '', '26.40']
Row 26: Bad row: ['VZ', '', '42.92']
Number of valid rows processed: 20
```

Lassen Sie uns auch überprüfen, ob das Programm mit gültigen Daten korrekt funktioniert. Führen Sie den folgenden Code im Python-Interpreter aus:

```python
valid_port = read_csv_as_dicts('valid.csv', types=[str, int, float])
print(f"Number of valid rows processed: {len(valid_port)}")
```

Sie sollten sehen, dass alle Zeilen ohne Fehler verarbeitet werden. Hier ist ein Beispiel für die Ausgabe:

```
Number of valid rows processed: 17
```

Um den Python-Interpreter zu beenden, führen Sie den folgenden Befehl aus:

```python
exit()
```

Jetzt ist Ihr Code robuster. Er kann ungültige Daten elegant behandeln, indem er fehlerhafte Zeilen überspringt, anstatt abzustürzen. Dies macht Ihr Programm zuverlässiger und benutzerfreundlicher.
