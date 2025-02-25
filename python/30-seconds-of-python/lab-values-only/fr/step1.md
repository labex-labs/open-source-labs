# Valeurs de dictionnaire

On vous donne un dictionnaire aplati, et vous devez créer une fonction qui renvoie une liste aplatie de toutes les valeurs du dictionnaire. Votre tâche est d'implémenter la fonction `values_only(flat_dict)` qui prend en argument un dictionnaire aplati et renvoie une liste de toutes les valeurs du dictionnaire.

Pour résoudre ce problème, vous pouvez utiliser la méthode `dict.values()` pour renvoyer les valeurs du dictionnaire donné. Ensuite, vous pouvez convertir le résultat en une liste en utilisant la fonction `list()`.

```python
def values_only(flat_dict):
  return list(flat_dict.values())
```

```python
ages = {
  'Peter': 10,
  'Isabel': 11,
  'Anna': 9,
}
values_only(ages) # [10, 11, 9]
```
