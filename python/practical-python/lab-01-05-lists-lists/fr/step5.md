# Tri d'une liste

Les listes peuvent être triées "en place".

```python
s = [10, 1, 7, 3]
s.sort()                    # [1, 3, 7, 10]

# Tri dans l'ordre inverse
s = [10, 1, 7, 3]
s.sort(reverse=True)        # [10, 7, 3, 1]

# Cela fonctionne avec n'importe quel type de données ordonnée
s = ['foo', 'bar','spam']
s.sort()                    # ['bar', 'foo','spam']
```

Utilisez `sorted()` si vous préférez créer une nouvelle liste :

```python
t = sorted(s)               # s est inchangé, t contient les valeurs triées
```
