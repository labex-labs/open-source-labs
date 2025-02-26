# Noms de fichiers vs Itérables

Comparez ces deux programmes qui renvoient la même sortie.

```python
# Fournir un nom de fichier
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
# Fournir des lignes
def read_data(lines):
    records = []
    for line in lines:
     ...
        records.append(r)
    return records

with open('file.csv') as f:
    d = read_data(f)
```

- Quelle de ces fonctions préférez-vous? Pourquoi?
- Quelle de ces fonctions est la plus flexible?
