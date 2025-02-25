# Collection est vide

Écrivez une fonction Python appelée `is_empty(val)` qui prend une valeur en tant que paramètre et renvoie `True` si la valeur est une séquence ou une collection vide, et `False` sinon.

Pour vérifier si une séquence ou une collection est vide, vous pouvez utiliser l'opérateur `not` pour tester la valeur de vérité de la séquence ou de la collection fournie. Si la séquence ou la collection est vide, l'opérateur `not` renverra `True`.

Votre fonction devrait être capable de gérer les types de séquences et de collections suivants :

- Listes
- Tuples
- Ensembles
- Dictionnaires
- Chaînes de caractères
- Plages

```python
def is_empty(val):
  return not val
```

```python
is_empty([]) # True
is_empty({}) # True
is_empty('') # True
is_empty(set()) # True
is_empty(range(0)) # True
is_empty([1, 2]) # False
is_empty({ 'a': 1, 'b': 2 }) # False
is_empty('text') # False
is_empty(set([1, 2])) # False
is_empty(range(2)) # False
```
