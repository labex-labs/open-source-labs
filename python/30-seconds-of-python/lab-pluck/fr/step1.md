# Extraire des valeurs d'une liste de dictionnaires

Écrivez une fonction `pluck(lst, key)` qui prend en arguments une liste de dictionnaires `lst` et une clé `key` et renvoie une liste de valeurs correspondant à la clé spécifiée.

Vous devez :

- Utiliser une compréhension de liste et `dict.get()` pour obtenir la valeur de `key` pour chaque dictionnaire dans `lst`.
- La fonction doit renvoyer une liste vide si la liste d'entrée est vide ou si la clé spécifiée n'est pas présente dans aucun des dictionnaires.

```python
def pluck(lst, key):
  return [x.get(key) for x in lst]
```

```python
simpsons = [
  { 'name': 'lisa', 'age': 8 },
  { 'name': 'homer', 'age': 36 },
  { 'name':'marge', 'age': 34 },
  { 'name': 'bart', 'age': 10 }
]
pluck(simpsons, 'age') # [8, 36, 34, 10]
```
