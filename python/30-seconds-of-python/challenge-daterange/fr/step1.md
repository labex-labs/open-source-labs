# Défi de plage de dates

## Problème

Écrivez une fonction Python appelée `daterange(start, end)` qui prend deux objets `datetime.date` en arguments et renvoie une liste de toutes les dates comprises entre elles. La liste devrait inclure la date de début mais pas la date de fin.

Pour résoudre ce problème, vous pouvez suivre ces étapes :

1. Utilisez `datetime.timedelta.days` pour obtenir le nombre de jours entre `start` et `end`.
2. Utilisez `int()` pour convertir le résultat en entier et `range()` pour itérer sur chaque jour.
3. Utilisez une compréhension de liste et `datetime.timedelta` pour créer une liste d'objets `datetime.date`.

## Exemple

```python
from datetime import date

daterange(date(2020, 10, 1), date(2020, 10, 5))
# [date(2020, 10, 1), date(2020, 10, 2), date(2020, 10, 3), date(2020, 10, 4)]
```
