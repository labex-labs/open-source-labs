# Construcción de listas

Construir una lista desde cero.

```python
records = []  # Lista vacía inicial

# Use.append() para agregar más elementos
records.append(('GOOG', 100, 490.10))
records.append(('IBM', 50, 91.3))
...
```

Un ejemplo al leer registros de un archivo.

```python
records = []  # Lista vacía inicial

with open('portfolio.csv', 'rt') as f:
    next(f) # Saltar el encabezado
    for line in f:
        row = line.split(',')
        records.append((row[0], int(row[1]), float(row[2])))
```
