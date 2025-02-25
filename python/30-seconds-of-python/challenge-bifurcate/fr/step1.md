# Bifurquer une liste

## Problème

Écrivez une fonction `bifurcate(lst, filtre)` qui prend une liste `lst` et un filtre `filtre` en entrée et renvoie une liste de deux listes. La première liste devrait contenir les éléments de `lst` qui passent le filtre, et la seconde liste devrait contenir les éléments qui ne le passent pas.

Pour implémenter cette fonction, vous pouvez utiliser une compréhension de liste et la fonction `zip()`. La fonction `zip()` prend deux listes ou plus en entrée et renvoie une liste de tuples, où chaque tuple contient les éléments correspondants de chaque liste. Par exemple, `zip([1, 2, 3], [4, 5, 6])` renvoie `[(1, 4), (2, 5), (3, 6)]`.

Vous pouvez utiliser cette fonction pour itérer simultanément sur `lst` et `filtre` et ajouter les éléments à la liste appropriée selon qu'ils passent le filtre ou non.

## Exemple

```python
bifurcate(['beep', 'boop', 'foo', 'bar'], [True, True, False, True])
# Sortie : [['beep', 'boop', 'bar'], ['foo']]
```

Dans l'exemple ci-dessus, le filtre est `[True, True, False, True]`. Les deux premiers éléments de `lst` passent le filtre, donc ils sont ajoutés à la première liste. Le troisième élément ne passe pas le filtre, donc il est ajouté à la seconde liste. Le quatrième élément passe le filtre, donc il est ajouté à la première liste.
