# Extraire des valeurs d'une liste de dictionnaires

## Problème

Écrivez une fonction `pluck(lst, key)` qui prend une liste de dictionnaires `lst` et une clé `key` en arguments et renvoie une liste des valeurs correspondant à la clé spécifiée.

Vous devez :

- Utiliser une compréhension de liste et `dict.get()` pour obtenir la valeur de `key` pour chaque dictionnaire dans `lst`.
- La fonction doit renvoyer une liste vide si la liste d'entrée est vide ou si la clé spécifiée n'est pas présente dans aucun des dictionnaires.

## Exemple

```python
simpsons = [
  { 'name': 'lisa', 'age': 8 },
  { 'name': 'homer', 'age': 36 },
  { 'name':'marge', 'age': 34 },
  { 'name': 'bart', 'age': 10 }
]
print(pluck(simpsons, 'age')) # [8, 36, 34, 10]
```
