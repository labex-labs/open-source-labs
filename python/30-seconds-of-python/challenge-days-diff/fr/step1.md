# Différence de dates en jours

## Problème

Écrivez une fonction `days_diff(start, end)` qui prend deux objets de date en entrée et renvoie le nombre de jours entre eux. La fonction devrait soustraire `start` de `end` et utiliser `datetime.timedelta.days` pour obtenir la différence de jours.

## Exemple

```python
from datetime import date

assert days_diff(date(2020, 10, 25), date(2020, 10, 28)) == 3
assert days_diff(date(2021, 1, 1), date(2021, 1, 1)) == 0
assert days_diff(date(2021, 1, 1), date(2021, 1, 2)) == 1
```
