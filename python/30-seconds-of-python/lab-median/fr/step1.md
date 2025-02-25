# Médiane

Écrivez une fonction Python appelée `find_median` qui prend une liste de nombres en argument et renvoie la médiane de la liste. Votre fonction doit effectuer les étapes suivantes :

1. Trier les nombres de la liste à l'aide de `list.sort()`.
2. Trouver la médiane, qui est soit l'élément du milieu de la liste si la longueur de la liste est impaire, soit la moyenne des deux éléments du milieu si la longueur de la liste est paire.
3. Retourner la médiane.

Votre fonction ne doit pas utiliser de bibliothèques ou de fonctions Python intégrées qui résolvent directement le problème.

```python
def median(list):
  list.sort()
  list_length = len(list)
  if list_length % 2 == 0:
    return (list[int(list_length / 2) - 1] + list[int(list_length / 2)]) / 2
  return float(list[int(list_length / 2)])
```

```python
median([1, 2, 3]) # 2.0
median([1, 2, 3, 4]) # 2.5
```
