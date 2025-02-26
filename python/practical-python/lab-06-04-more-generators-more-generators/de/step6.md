# Übung 6.15: Codevereinfachung

Generatorausdrücke sind oft eine nützliche Ersatzmethode für kleine Generatorfunktionen. Beispielsweise anstatt eine Funktion wie diese zu schreiben:

```python
def filter_symbols(rows, names):
    for row in rows:
        if row['name'] in names:
            yield row
```

Können Sie etwas wie Folgendes schreiben:

```python
rows = (row for row in rows if row['name'] in names)
```

Ändern Sie das `ticker.py`-Programm, um Generatorausdrücke an geeigneten Stellen zu verwenden.
