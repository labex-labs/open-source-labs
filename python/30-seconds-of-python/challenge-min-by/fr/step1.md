# Trouver la valeur minimale d'une liste en fonction d'une fonction

## Problème

Écrivez une fonction appelée `min_by(lst, fn)` qui prend une liste `lst` et une fonction `fn` en arguments. La fonction devrait mapper chaque élément de la liste à une valeur en utilisant la fonction fournie, puis renvoyer la valeur minimale.

## Exemple

```python
min_by([{ 'n': 4 }, { 'n': 2 }, { 'n': 8 }, { 'n': 6 }], lambda v : v['n']) # 2
```

Dans l'exemple ci-dessus, la fonction `min_by()` est appelée avec une liste de dictionnaires et une fonction lambda qui extrait la valeur de la clé `'n'` de chaque dictionnaire. La fonction renvoie la valeur minimale de la liste, qui est `2`.
