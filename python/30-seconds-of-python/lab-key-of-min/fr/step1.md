# Clé de la valeur minimale

Écrivez une fonction `clé_de_min(d)` qui prend en argument un dictionnaire `d` et renvoie la clé de la valeur minimale dans le dictionnaire.

Pour résoudre ce problème, vous pouvez utiliser la fonction intégrée `min()` avec le paramètre `clé` défini sur `dict.get()`. Cela renverra la clé de la valeur minimale dans le dictionnaire.

```python
def clé_de_min(d):
  return min(d, clé = d.get)
```

```python
clé_de_min({'a':4, 'b':0, 'c':13}) # b
```
