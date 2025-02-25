# Clé de la valeur maximale

## Problème

Écrivez une fonction `clé_de_max(d)` qui prend un dictionnaire `d` en argument et renvoie la clé de la valeur maximale dans le dictionnaire. Si plusieurs clés ont la même valeur maximale, renvoyez l'une d'entre elles.

Pour résoudre ce problème, vous pouvez utiliser la fonction `max()` avec le paramètre `clé` défini sur `dict.get()`. Cela renverra la clé de la valeur maximale dans le dictionnaire.

## Exemple

```python
clé_de_max({'a':4, 'b':0, 'c':13}) # 'c'
```
