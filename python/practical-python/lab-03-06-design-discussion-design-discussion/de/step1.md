# Dateinamen versus Iterierbare

Vergleichen Sie diese beiden Programme, die das gleiche Ergebnis liefern.

```python
# Geben Sie einen Dateinamen an
def read_data(filename):
    records = []
    with open(filename) as f:
        for line in f:
         ...
            records.append(r)
    return records

d = read_data('file.csv')
```

```python
# Geben Sie Zeilen an
def read_data(lines):
    records = []
    for line in lines:
     ...
        records.append(r)
    return records

with open('file.csv') as f:
    d = read_data(f)
```

- Welche dieser Funktionen bevorzugen Sie? Warum?
- Welche dieser Funktionen ist flexibler?
