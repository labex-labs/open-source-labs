# Vorbereitung

In der Datei `reader.py` gibt es eine zentrale Funktion `convert_csv()`, die den Großteil der Arbeit erledigt. Diese Funktion stürzt ab, wenn Sie sie auf Daten mit fehlenden oder fehlerhaften Daten ausführen. Beispielsweise:

```bash
$ python
>>> from reader import read_csv_as_dicts
```

```python
>>> port = read_csv_as_dicts('missing.csv', types=[str, int, float])
Fehlermeldung (letzte aufgerufene Zeile zuerst):
  Datei "<stdin>", Zeile 1, in <module>
  Datei "reader.py", Zeile 24, in read_csv_as_dicts
    return csv_as_dicts(file, types, headers=headers)
  Datei "reader.py", Zeile 13, in csv_as_dicts
    lambda headers, row: { name: func(val) for name, func, val in zip(headers, types, row) })
  Datei "reader.py", Zeile 9, in convert_csv
    return list(map(lambda row: converter(headers, row), rows))
  Datei "reader.py", Zeile 9, in <lambda>
    return list(map(lambda row: converter(headers, row), rows))
  Datei "reader.py", Zeile 13, in <lambda>
    lambda headers, row: { name: func(val) for name, func, val in zip(headers, types, row) })
  Datei "reader.py", Zeile 13, in <dictcomp>
    lambda headers, row: { name: func(val) for name, func, val in zip(headers, types, row) })
Wertfehler: ungültiges Literal für int() mit Basis 10: ''
>>>
```
