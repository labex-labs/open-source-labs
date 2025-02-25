# Index de l'élément maximal

## Problème

Écrivez une fonction `max_element_index(arr)` qui prend une liste `arr` en argument et renvoie l'index de l'élément ayant la valeur maximale. Si plusieurs éléments ont la valeur maximale, renvoyez l'index de la première occurrence.

Pour résoudre ce problème, vous pouvez suivre ces étapes :

1. Utilisez la fonction intégrée `max()` pour trouver la valeur maximale dans la liste.
2. Utilisez la fonction intégrée `list.index()` pour trouver l'index de la première occurrence de la valeur maximale dans la liste.
3. Renvoyez l'index.

## Exemple

```python
max_element_index([5, 8, 9, 7, 10, 3, 0]) # 4
```

Dans cet exemple, la valeur maximale dans la liste `[5, 8, 9, 7, 10, 3, 0]` est `10`, qui se trouve à l'index `4`. Par conséquent, la fonction devrait renvoyer `4`.
