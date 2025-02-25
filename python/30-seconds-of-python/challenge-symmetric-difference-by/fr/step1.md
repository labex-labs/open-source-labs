# Différence symétrique basée sur une fonction

## Problème

Écrivez une fonction `symmetric_difference_by(a, b, fn)` qui prend deux listes `a` et `b`, et une fonction `fn`. La fonction devrait renvoyer une nouvelle liste contenant tous les éléments qui se trouvent dans l'une ou l'autre des listes d'origine, mais pas dans les deux, après avoir appliqué la fonction fournie à chaque élément de liste des deux.

Pour résoudre ce problème, vous pouvez suivre ces étapes :

1. Créez un `ensemble` en appliquant `fn` à chaque élément de chaque liste.
2. Utilisez une compréhension de liste en combinaison avec `fn` sur chacune d'elles pour ne conserver que les valeurs qui ne sont pas contenues dans l'ensemble précédemment créé de l'autre.
3. Concaténez les deux listes obtenues à l'étape 2.

La fonction devrait avoir les paramètres suivants :

- `a` : une liste d'éléments
- `b` : une liste d'éléments
- `fn` : une fonction qui prend un élément et renvoie une nouvelle valeur

La fonction devrait renvoyer une nouvelle liste contenant tous les éléments qui se trouvent dans l'une ou l'autre des listes d'origine, mais pas dans les deux, après avoir appliqué la fonction fournie à chaque élément de liste des deux.

## Exemple

```python
from math import floor

assert symmetric_difference_by([2.1, 1.2], [2.3, 3.4], floor) == [1.2, 3.4]
```
