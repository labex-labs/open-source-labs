# Différence de dates

Écrivez une fonction appelée `months_diff(start, end)` qui prend en compte deux objets de date et renvoie la différence de mois entre eux. La fonction devrait :

1. Soustraire `start` de `end` et utiliser `datetime.timedelta.days` pour obtenir la différence en jours.
2. Diviser par `30` et utiliser `math.ceil()` pour obtenir la différence en mois (arrondie à l'entier supérieur).

```python
from math import ceil

def months_diff(start, end):
  return ceil((end - start).days / 30)
```

```python
from datetime import date

months_diff(date(2020, 10, 28), date(2020, 11, 25)) # 1
```
