# Exercice 6.15 : Simplification du code

Les expressions de générateur sont souvent un remplacement utile pour de petites fonctions génératrices. Par exemple, au lieu d'écrire une fonction comme celle-ci :

```python
def filter_symbols(rows, names):
    for row in rows:
        if row['name'] in names:
            yield row
```

Vous pourriez écrire quelque chose comme ceci :

```python
rows = (row for row in rows if row['name'] in names)
```

Modifiez le programme `ticker.py` pour utiliser des expressions de générateur le cas échéant.
