# Map List to Dictionary (Mapper une liste en dictionnaire)

Écrivez une fonction Python appelée `map_dictionary(itr, fn)` qui prend deux paramètres :

- `itr` : une liste de valeurs
- `fn` : une fonction qui prend une valeur en entrée et renvoie une valeur en sortie

La fonction doit renvoyer un dictionnaire où les paires clé-valeur sont constituées de la valeur originale comme clé et du résultat de la fonction comme valeur.

Pour résoudre ce problème, suivez ces étapes :

1. Utilisez `map()` pour appliquer `fn` à chaque valeur de la liste.
2. Utilisez `zip()` pour associer les valeurs originales aux valeurs produites par `fn`.
3. Utilisez `dict()` pour renvoyer un dictionnaire approprié.

```python
def map_dictionary(itr, fn):
  return dict(zip(itr, map(fn, itr)))
```

```python
map_dictionary([1, 2, 3], lambda x: x * x) # { 1: 1, 2: 4, 3: 9 }
```
