# Nombre dans la plage

## Problème

Écrivez une fonction `in_range(n, start, end = 0)` qui prend trois paramètres :

- `n` : un nombre à vérifier s'il se situe dans la plage
- `start` : le début de la plage
- `end` : la fin de la plage (optionnel, valeur par défaut est 0)

La fonction devrait renvoyer `True` si le nombre `n` donné se situe dans la plage spécifiée, et `False` sinon. Si le paramètre `end` n'est pas spécifié, la plage est considérée comme allant de `0` à `start`.

## Exemple

```python
in_range(3, 2, 5) # True
in_range(3, 4) # True
in_range(2, 3, 5) # False
in_range(3, 2) # False
```
