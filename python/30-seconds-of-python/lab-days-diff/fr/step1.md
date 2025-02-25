# Date Difference in Days

Écrivez une fonction `days_diff(start, end)` qui prend deux objets de date en entrée et renvoie le nombre de jours entre elles. La fonction devrait soustraire `start` de `end` et utiliser `datetime.timedelta.days` pour obtenir la différence en jours.

```python
def days_diff(start, end):
  return (end - start).days
```

```python
from datetime import date

days_diff(date(2020, 10, 25), date(2020, 10, 28)) # 3
```
