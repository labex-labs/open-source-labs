# Nombres de archivos versus Iterables

Compara estos dos programas que devuelven la misma salida.

```python
# Proporciona un nombre de archivo
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
# Proporciona líneas
def read_data(lines):
    records = []
    for line in lines:
     ...
        records.append(r)
    return records

with open('file.csv') as f:
    d = read_data(f)
```

- ¿Cuál de estas funciones prefieres? ¿Por qué?
- ¿Cuál de estas funciones es más flexible?
