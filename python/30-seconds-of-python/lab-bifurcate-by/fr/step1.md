# Diviser une liste en fonction d'une fonction

Écrivez une fonction `bifurcate_by(lst, fn)` qui prend une liste `lst` et une fonction de filtrage `fn` en arguments. La fonction doit diviser la liste en deux groupes en fonction du résultat de la fonction de filtrage. Si la fonction de filtrage renvoie une valeur vraie pour un élément, celui-ci doit être ajouté au premier groupe. Sinon, il doit être ajouté au second groupe.

Votre fonction doit renvoyer une liste de deux listes, où la première liste contient tous les éléments pour lesquels la fonction de filtrage a renvoyé une valeur vraie, et la seconde liste contient tous les éléments pour lesquels la fonction de filtrage a renvoyé une valeur fausse.

Utilisez une compréhension de liste pour ajouter des éléments aux groupes, en fonction de la valeur renvoyée par `fn` pour chaque élément.

```python
def bifurcate_by(lst, fn):
  return [
    [x for x in lst if fn(x)],
    [x for x in lst if not fn(x)]
  ]
```

```python
bifurcate_by(['beep', 'boop', 'foo', 'bar'], lambda x: x[0] == 'b')
# [ ['beep', 'boop', 'bar'], ['foo'] ]
```
