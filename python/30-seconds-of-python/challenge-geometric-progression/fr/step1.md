# Défi de progression géométrique

## Problème

Écrivez une fonction appelée `geometric_progression` qui prend trois paramètres :

- `end` : un entier représentant la fin de la plage (inclusive)
- `start` : un entier optionnel représentant le début de la plage (inclusive), avec une valeur par défaut de `1`
- `step` : un entier optionnel représentant le ratio commun entre deux termes, avec une valeur par défaut de `2`

La fonction devrait renvoyer une liste contenant les nombres dans la plage spécifiée où le ratio entre deux termes est `step`. La liste devrait commencer par `start` et finir par `end`.

Si `step` est égal à `1`, la fonction devrait renvoyer une erreur.

Vous devriez utiliser `range()`, `math.log()` et `math.floor()` et une compréhension de liste pour créer une liste de la longueur appropriée, en appliquant le pas à chaque élément.

## Exemple

```python
geometric_progression(256) # [1, 2, 4, 8, 16, 32, 64, 128, 256]
geometric_progression(256, 3) # [3, 6, 12, 24, 48, 96, 192]
geometric_progression(256, 1, 4) # [1, 4, 16, 64, 256]
```
