# Vérification des doublons dans une fonction de liste

## Problème

Écrivez une fonction Python appelée `has_duplicates(lst)` qui prend une liste en argument et renvoie `True` si la liste contient des éléments dupliqués, sinon renvoie `False`.

Pour résoudre ce problème, vous pouvez suivre ces étapes :

1. Convertissez la liste en ensemble pour supprimer les doublons.
2. Comparez la longueur de l'ensemble avec la longueur de la liste d'origine.
3. Si les longueurs sont égales, alors la liste n'a pas de doublons, sinon elle en a.

## Exemple

```python
has_duplicates([1, 2, 3, 4, 5]) # False
has_duplicates([1, 2, 3, 4, 5, 5]) # True
has_duplicates(['apple', 'banana', 'orange', 'banana']) # True
has_duplicates([]) # False
```
