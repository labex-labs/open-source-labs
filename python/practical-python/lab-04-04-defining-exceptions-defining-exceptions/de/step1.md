# Übung 4.11: Definieren einer benutzerdefinierten Ausnahme

Es ist oft eine gute Praxis für Bibliotheken, ihre eigenen Ausnahmen zu definieren.

Dadurch ist es einfacher, zwischen Python-Ausnahmen zu unterscheiden, die als Reaktion auf übliche Programmierfehler ausgelöst werden, und Ausnahmen, die von einer Bibliothek absichtlich ausgelöst werden, um ein bestimmtes Verwendungsproblem anzuzeigen.

Ändern Sie die Funktion `create_formatter()` aus der letzten Übung so, dass sie eine benutzerdefinierte `FormatError`-Ausnahme auslöst, wenn der Benutzer einen ungültigen Formatnamen angibt.

Beispiel:

```python
>>> from tableformat import create_formatter
>>> formatter = create_formatter('xls')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "tableformat.py", line 80, in create_formatter
    raise FormatError(f"Unknown table format {name}")
tableformat.FormatError: Unknown table format xls
>>>
```
