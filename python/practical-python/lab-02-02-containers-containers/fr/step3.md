# Construction de listes

Création d'une liste à partir de zéro.

```python
records = []  # Liste initialement vide

# Utilisez.append() pour ajouter plus d'éléments
records.append(('GOOG', 100, 490.10))
records.append(('IBM', 50, 91.3))
...
```

Un exemple lors de la lecture de records à partir d'un fichier.

```python
records = []  # Liste initialement vide

with open('portfolio.csv', 'rt') as f:
    next(f) # Passez l'en-tête
    for line in f:
        row = line.split(',')
        records.append((row[0], int(row[1]), float(row[2])))
```
