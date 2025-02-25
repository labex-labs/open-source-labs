# Index de l'élément minimum

## Problème

Écrivez une fonction `min_element_index(arr)` qui prend une liste d'entiers `arr` en argument et renvoie l'index de l'élément ayant la valeur minimale dans la liste.

Pour résoudre ce problème, vous pouvez utiliser la fonction `min()` pour obtenir la valeur minimale dans la liste puis utiliser la méthode `list.index()` pour renvoyer son index.

## Exemple

```python
min_element_index([3, 5, 2, 6, 10, 7, 9]) # 2
```

Dans cet exemple, la valeur minimale dans la liste `[3, 5, 2, 6, 10, 7, 9]` est `2`, qui se trouve à l'index `2`.
