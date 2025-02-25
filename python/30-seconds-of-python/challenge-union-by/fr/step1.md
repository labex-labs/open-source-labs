# Union de listes basée sur une fonction

## Problème

Écrivez une fonction `union_by(a, b, fn)` qui prend deux listes `a` et `b`, et une fonction `fn`. La fonction devrait renvoyer une liste qui contient chaque élément qui existe dans l'une ou l'autre des deux listes une fois, après avoir appliqué la fonction fournie à chaque élément des deux.

Pour résoudre ce problème, vous pouvez suivre ces étapes :

1. Créez un `ensemble` en appliquant `fn` à chaque élément de `a`.
2. Utilisez une compréhension de liste en combinaison avec `fn` sur `b` pour ne conserver que les valeurs qui ne sont pas contenues dans l'ensemble précédemment créé, `_a`.
3. Enfin, créez un `ensemble` à partir du résultat précédent et `a` et transformez-le en une `liste`.

La fonction devrait avoir les paramètres d'entrée suivants :

- `a` : une liste d'éléments
- `b` : une liste d'éléments
- `fn` : une fonction qui prend un élément et renvoie une valeur

La fonction devrait renvoyer une liste d'éléments.

## Exemple

Voici un exemple de ce que devrait faire `union_by()` :

```python
from math import floor

union_by([2.1], [1.2, 2.3], floor) # [2.1, 1.2]
```

Dans cet exemple, `union_by()` prend deux listes `[2.1]` et `[1.2, 2.3]`, et une fonction `floor()`. La fonction applique `floor()` à chaque élément des deux listes, créant un ensemble `{2}`. Ensuite, elle utilise une compréhension de liste pour ne conserver que les valeurs qui ne sont pas contenues dans l'ensemble, qui est `[1.2]`. Enfin, elle crée un ensemble à partir du résultat précédent et `[2.1]`, qui est `{1.2, 2.1}`, et le transforme en une liste `[1.2, 2.1]`.
