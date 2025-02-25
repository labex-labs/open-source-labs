# Somme d'une liste basée sur une fonction

## Problème

Écrivez une fonction `sum_by(lst, fn)` qui prend une liste `lst` et une fonction `fn` en arguments. La fonction devrait mapper chaque élément de la liste à une valeur à l'aide de la fonction fournie, et renvoyer la somme des valeurs.

## Exemple

```python
sum_by([{ 'n': 4 }, { 'n': 2 }, { 'n': 8 }, { 'n': 6 }], lambda v : v['n']) # 20
```

Dans l'exemple ci-dessus, la fonction `sum_by()` prend une liste de dictionnaires et une fonction lambda qui extrait la valeur de la clé `'n'` de chaque dictionnaire. La fonction map chaque dictionnaire à sa valeur `'n'` et renvoie la somme des valeurs, qui est `20`.
