# Vérifiez si chaque élément de la liste est considéré comme faux (`falsy`)

## Problème

Écrivez une fonction Python appelée `none(lst, fn = lambda x: x)` qui prend une liste `lst` et une fonction optionnelle `fn` en arguments. La fonction devrait renvoyer `True` si chaque élément de la liste est considéré comme faux (`falsy`), et `False` sinon. Si la fonction optionnelle `fn` est fournie, elle devrait être utilisée pour déterminer la vérité ou non de chaque élément de la liste.

Pour déterminer si un élément est considéré comme faux (`falsy`), vous pouvez utiliser les mêmes règles que la fonction `bool()` de Python. En général, les valeurs suivantes sont considérées comme fausses (`falsy`):

- `False`
- `None`
- `0` (entier)
- `0.0` (flottant)
- `''` (chaîne de caractères vide)
- `[]` (liste vide)
- `{}` (dictionnaire vide)
- `()` (tuple vide)
- `set()` (ensemble vide)

Si la fonction optionnelle `fn` est fournie, elle devrait prendre un argument et renvoyer une valeur booléenne. La fonction sera appelée pour chaque élément de la liste, et la valeur de retour sera utilisée pour déterminer la vérité ou non de l'élément.

## Exemple

```python
assert none([0, 1, 2, 0], lambda x: x >= 2 ) == False
assert none([0, 0, 0]) == True
```
