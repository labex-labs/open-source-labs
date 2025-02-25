# Übliche Muster zum Lesen von Dateidaten

Eine ganze Datei als String auf einmal lesen.

```python
with open('foo.txt', 'rt') as file:
    data = file.read()
    # `data` ist ein String mit allem Text in `foo.txt`
```

Eine Datei Zeile für Zeile durch Iteration lesen.

```python
with open(filename, 'rt') as file:
    for line in file:
        # Verarbeiten Sie die Zeile
```
