# Différence symétrique

## Problème

Écrivez une fonction `symmetric_difference(a, b)` qui prend deux listes en arguments et renvoie leur différence symétrique sous forme de liste. La fonction ne doit pas éliminer les valeurs dupliquées.

Pour résoudre ce problème, vous pouvez suivre ces étapes :

1. Créez un ensemble à partir de chaque liste.
2. Utilisez une compréhension de liste sur chacune d'entre elles pour ne conserver que les valeurs qui ne sont pas contenues dans l'ensemble précédemment créé de l'autre.
3. Concaténez les deux listes obtenues à l'étape 2.

## Exemple

```python
symmetric_difference([1, 2, 3], [1, 2, 4]) # [3, 4]
```
