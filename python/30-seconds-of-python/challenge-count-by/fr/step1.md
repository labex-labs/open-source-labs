# Compter les éléments regroupés

## Problème

Écrivez une fonction `count_by(lst, fn = lambda x: x)` qui prend une liste `lst` et une fonction `fn` en arguments. La fonction devrait regrouper les éléments de la liste sur la base de la fonction donnée et renvoyer un dictionnaire avec le compte d'éléments dans chaque groupe.

Pour résoudre ce problème, vous pouvez suivre ces étapes :

1. Initialisez un dictionnaire à l'aide de `collections.defaultdict`.
2. Utilisez `map()` pour appliquer la fonction donnée à chaque élément de la liste.
3. Itérez sur les valeurs mappées et augmentez le compte de chaque élément dans le dictionnaire.

La fonction devrait renvoyer le dictionnaire résultant.

## Exemple

```python
count_by([6.1, 4.2, 6.3], floor) # {6: 2, 4: 1}
count_by(['one', 'two', 'three'], len) # {3: 2, 5: 1}
```

Dans le premier exemple, la fonction `floor` est utilisée pour regrouper les éléments de la liste `[6.1, 4.2, 6.3]`. Le dictionnaire résultant a deux clés : `6` et `4`, avec respectivement les valeurs `2` et `1`.

Dans le second exemple, la fonction `len` est utilisée pour regrouper les éléments de la liste `['one', 'two', 'three']`. Le dictionnaire résultant a deux clés : `3` et `5`, avec respectivement les valeurs `2` et `1`.
