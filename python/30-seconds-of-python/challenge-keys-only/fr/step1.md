# Clés de dictionnaire

## Problème

Écrivez une fonction `keys_only(flat_dict)` qui prend un dictionnaire plat en entrée et renvoie une liste de toutes ses clés.

Pour résoudre ce problème, vous pouvez suivre ces étapes :

1. Utilisez `dict.keys()` pour renvoyer les clés dans le dictionnaire donné.
2. Retournez une `list()` du résultat précédent.

## Exemple

```python
ages = {
  'Peter': 10,
  'Isabel': 11,
  'Anna': 9,
}
keys_only(ages) # ['Peter', 'Isabel', 'Anna']
```
