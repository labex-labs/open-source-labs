# Somme des puissances - Défi

## Problème

Écrivez une fonction Python appelée `sum_of_powers` qui prend trois paramètres :

- `end` - un entier représentant la fin de la plage (inclusif)
- `power` - un entier représentant la puissance à laquelle chaque nombre de la plage doit être élevé (valeur par défaut est 2)
- `start` - un entier représentant le début de la plage (valeur par défaut est 1)

La fonction devrait retourner la somme des puissances de tous les nombres de `start` à `end` (y compris les deux).

Pour résoudre ce problème, vous pouvez suivre ces étapes :

1. Utilisez `range()` en combinaison avec une compréhension de liste pour créer une liste d'éléments dans la plage souhaitée élevés à la `power` donnée.
2. Utilisez `sum()` pour additionner les valeurs ensemble.

## Exemple

```python
sum_of_powers(10) # renvoie 385
sum_of_powers(10, 3) # renvoie 3025
sum_of_powers(10, 3, 5) # renvoie 2925
```
