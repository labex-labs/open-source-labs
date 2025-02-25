# Fusionner des dictionnaires

Écrivez une fonction `merge_dictionaries(*dicts)` qui prend deux ou plusieurs dictionnaires en arguments et renvoie un nouveau dictionnaire qui contient toutes les paires clé-valeur des dictionnaires d'entrée.

Votre fonction devrait créer un nouveau dictionnaire et parcourir les dictionnaires d'entrée, en utilisant `dictionary.update()` pour ajouter les paires clé-valeur de chacun au résultat.

```python
def merge_dictionaries(*dicts):
  res = dict()
  for d in dicts:
    res.update(d)
  return res
```

```python
ages_one = {
  'Peter': 10,
  'Isabel': 11,
}
ages_two = {
  'Anna': 9
}
merge_dictionaries(ages_one, ages_two)
# { 'Peter': 10, 'Isabel': 11, 'Anna': 9 }
```
