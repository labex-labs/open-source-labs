# Liste étalée

## Problème

Écrivez une fonction appelée `spread(arg)` qui prend une liste en argument et renvoie une nouvelle liste qui contient tous les éléments de la liste d'origine, aplatis. Si un élément de la liste d'origine est une liste en elle-même, ses éléments doivent être ajoutés individuellement à la nouvelle liste. La fonction ne doit pas modifier la liste d'origine.

Pour implémenter la fonction, vous devriez parcourir les éléments de la liste d'origine et utiliser l'opérateur de diffusion pour ajouter les éléments à la nouvelle liste. Si un élément est une liste, vous devriez utiliser la méthode `extend()` pour ajouter ses éléments à la nouvelle liste. Si un élément n'est pas une liste, vous devriez utiliser la méthode `append()` pour l'ajouter à la nouvelle liste.

## Exemple

```python
spread([1, 2, 3, [4, 5, 6], [7], 8, 9]) # [1, 2, 3, 4, 5, 6, 7, 8, 9]
```
