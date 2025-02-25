# Intersection de listes basée sur une fonction

## Problème

Écrivez une fonction `intersection_by(a, b, fn)` qui prend deux listes `a` et `b`, et une fonction `fn`. La fonction devrait renvoyer une liste d'éléments qui existent dans les deux listes, après avoir appliqué la fonction fournie à chaque élément des deux listes.

### Entrée

- Deux listes `a` et `b` (1 <= len(a), len(b) <= 1000)
- Une fonction `fn` qui prend un argument et renvoie une valeur

### Sortie

- Une liste d'éléments qui existent dans les deux listes, après avoir appliqué la fonction fournie à chaque élément des deux listes.

## Exemple

```python
intersection_by([2.1, 1.2], [2.3, 3.4], floor) # [2.1]
```

### Remarque

Dans l'exemple ci-dessus, la fonction `floor()` est appliquée à chaque élément des deux listes. Les ensembles résultants sont `{2, 3}` et `{2, 1}`. L'intersection de ces ensembles est `{2}`, qui est ensuite renvoyé sous forme de liste.
