# Vérifier les doublons dans une liste

Écrivez une fonction Python appelée `has_duplicates(lst)` qui prend une liste en argument et renvoie `True` si la liste contient des doublons, et `False` sinon.

Pour résoudre ce problème, vous pouvez suivre les étapes suivantes :

1. Utilisez la fonction `set()` pour supprimer les doublons de la liste.
2. Comparez la longueur de la liste d'origine avec la longueur de l'ensemble. Si elles sont les mêmes, alors il n'y a pas de doublons. Si elles sont différentes, alors il y a des doublons.

```python
def has_duplicates(lst):
  return len(lst)!= len(set(lst))
```

```python
x = [1, 2, 3, 4, 5, 5]
y = [1, 2, 3, 4, 5]
has_duplicates(x) # True
has_duplicates(y) # False
```
