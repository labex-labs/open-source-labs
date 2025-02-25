# Map Dictionary Values

Écrivez une fonction `map_values(obj, fn)` qui prend un dictionnaire `obj` et une fonction `fn` en arguments et renvoie un nouveau dictionnaire avec les mêmes clés que le dictionnaire original et des valeurs générées en exécutant la fonction fournie pour chaque valeur.

```python
def map_values(obj, fn):
  return dict((k, fn(v)) for k, v in obj.items())
```

```python
users = {
  'fred': { 'user': 'fred', 'age': 40 },
  'pebbles': { 'user': 'pebbles', 'age': 1 }
}
map_values(users, lambda u : u['age']) # {'fred': 40, 'pebbles': 1}
```
