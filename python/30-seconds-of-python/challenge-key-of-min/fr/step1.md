# Clé de la valeur minimale

## Problème

Écrivez une fonction `clé_de_min(d)` qui prend un dictionnaire `d` en tant qu'argument et renvoie la clé de la valeur minimale dans le dictionnaire.

Pour résoudre ce problème, vous pouvez utiliser la fonction intégrée `min()` avec le paramètre `clé` défini sur `dict.get()`. Cela renverra la clé de la valeur minimale dans le dictionnaire.

## Exemple

```python
clé_de_min({'a':4, 'b':0, 'c':13}) # 'b'
```

Dans cet exemple, le dictionnaire `{'a':4, 'b':0, 'c':13}` est passé en argument à la fonction `clé_de_min()`. La fonction renvoie la clé `'b'`, qui correspond à la valeur minimale dans le dictionnaire.
