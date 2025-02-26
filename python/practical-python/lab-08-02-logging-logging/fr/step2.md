# Exceptions Revisitées

Dans les exercices, nous avons écrit une fonction `parse()` qui ressemblait à ceci :

```python
# fileparse.py
def parse(f, types=None, names=None, delimiter=None):
    records = []
    for line in f:
        line = line.strip()
        if not line: continue
        try:
            records.append(split(line,types,names,delimiter))
        except ValueError as e:
            print("Couldn't parse :", line)
            print("Reason :", e)
    return records
```

Prenons en compte l'énoncé `try-except`. Que devriez-vous faire dans le bloc `except`?

Devriez-vous afficher un message d'avertissement?

```python
try:
    records.append(split(line,types,names,delimiter))
except ValueError as e:
    print("Couldn't parse :", line)
    print("Reason :", e)
```

Ou l'ignorez-vous silencieusement?

```python
try:
    records.append(split(line,types,names,delimiter))
except ValueError as e:
    pass
```

Aucune des solutions n'est satisfaisante car vous voulez souvent les _deux_ comportements (sélectionnables par l'utilisateur).
