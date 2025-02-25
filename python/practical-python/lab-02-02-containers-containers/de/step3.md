# Listenkonstruktion

Listen von Grund auf erstellen.

```python
records = []  # Initiale leere Liste

# Verwenden Sie.append(), um weitere Elemente hinzuzufügen
records.append(('GOOG', 100, 490.10))
records.append(('IBM', 50, 91.3))
...
```

Ein Beispiel, wenn Sie Datensätze aus einer Datei lesen.

```python
records = []  # Initiale leere Liste

with open('portfolio.csv', 'rt') as f:
    next(f) # Überspringen Sie die Kopfzeile
    for line in f:
        row = line.split(',')
        records.append((row[0], int(row[1]), float(row[2])))
```
