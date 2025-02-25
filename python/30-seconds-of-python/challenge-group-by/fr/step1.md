# Regrouper les éléments d'une liste

## Problème

Écrivez une fonction `group_by(lst, fn)` qui prend une liste `lst` et une fonction `fn` en arguments et renvoie un dictionnaire où les clés sont les résultats de l'application de `fn` aux éléments de `lst` et les valeurs sont des listes d'éléments de `lst` qui produisent la clé correspondante lorsqu'on leur applique `fn`.

Par exemple, si nous avons une liste de nombres `[6.1, 4.2, 6.3]` et que nous voulons les regrouper par leur partie entière, nous pouvons utiliser la fonction `floor` du module `math` comme fonction de regroupement. La sortie attendue serait `{4: [4.2], 6: [6.1, 6.3]}`.

## Exemple

```python
from math import floor

group_by([6.1, 4.2, 6.3], floor) # {4: [4.2], 6: [6.1, 6.3]}
group_by(['one', 'two', 'three'], len) # {3: ['one', 'two'], 5: ['three']}
```
