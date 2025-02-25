# Fonction `enumerate()`

La fonction `enumerate` ajoute une valeur de compteur supplémentaire à une itération.

```python
names = ['Elwood', 'Jake', 'Curtis']
for i, name in enumerate(names):
    # Boucle avec i = 0, name = 'Elwood'
    # i = 1, name = 'Jake'
    # i = 2, name = 'Curtis'
```

La forme générale est `enumerate(sequence [, start = 0])`. `start` est facultatif. Un bon exemple d'utilisation de `enumerate()` est le suivi des numéros de ligne lors de la lecture d'un fichier :

```python
with open(filename) as f:
    for lineno, line in enumerate(f, start=1):
     ...
```

En fin de compte, `enumerate` n'est qu'un raccourci pratique pour :

```python
i = 0
for x in s:
    statements
    i += 1
```

Utiliser `enumerate` nécessite moins de frappe et est légèrement plus rapide.
