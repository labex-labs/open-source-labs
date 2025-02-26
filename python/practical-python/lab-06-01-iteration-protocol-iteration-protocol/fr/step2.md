# Itération : Protocole

Considérez l'instruction `for`.

```python
for x in obj:
    # instructions
```

Que se passe-t-il en dessous des couvertures?

```python
_iter = obj.__iter__()        # Obtenir l'objet itérateur
while True:
    try:
        x = _iter.__next__()  # Obtenir l'élément suivant
        # instructions...
    except StopIteration:     # Plus d'éléments
        break
```

Tous les objets qui fonctionnent avec la boucle `for` implémentent ce protocole d'itération de bas niveau.

Exemple : Itération manuelle sur une liste.

```python
>>> x = [1,2,3]
>>> it = x.__iter__()
>>> it
<listiterator object at 0x590b0>
>>> it.__next__()
1
>>> it.__next__()
2
>>> it.__next__()
3
>>> it.__next__()
Traceback (most recent call last):
File "<stdin>", line 1, in? StopIteration
>>>
```
