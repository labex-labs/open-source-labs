# Défi de différence de dates

## Problème

Écrivez une fonction appelée `months_diff(start, end)` qui prend deux objets de date et renvoie la différence en mois entre eux. La fonction doit :

1. Soustraire `start` de `end` et utiliser `datetime.timedelta.days` pour obtenir la différence en jours.
2. Diviser par `30` et utiliser `math.ceil()` pour obtenir la différence en mois (arrondie à l'en haut).

## Exemple

```python
from datetime import date

months_diff(date(2020, 10, 28), date(2020, 11, 25)) # 1
```
