# Défi de la médiane

## Problème

Écrivez une fonction Python appelée `find_median` qui prend une liste de nombres en argument et renvoie la médiane de la liste. Votre fonction doit effectuer les étapes suivantes :

1. Trier les nombres de la liste en utilisant `list.sort()`.
2. Trouver la médiane, qui est soit l'élément du milieu de la liste si la longueur de la liste est impaire, soit la moyenne des deux éléments du milieu si la longueur de la liste est paire.
3. Retourner la médiane.

Votre fonction ne doit pas utiliser de bibliothèques ou de fonctions Python intégrées qui résolvent directement le problème.

## Exemple

```python
find_median([1, 2, 3]) # 2.0
find_median([1, 2, 3, 4]) # 2.5
```
