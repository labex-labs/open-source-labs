# Date est un week-end

Écrivez une fonction `is_weekend(d)` qui prend un objet de date en entrée et renvoie `True` si la date donnée est un week-end, et `False` sinon. Si aucun argument n'est fourni, la fonction devrait utiliser la date actuelle.

Pour résoudre ce problème, vous pouvez suivre ces étapes :

1. Utilisez la méthode `datetime.datetime.weekday()` pour obtenir le jour de la semaine sous forme d'un entier.
2. Vérifiez si le jour de la semaine est supérieur à `4`. Si c'est le cas, renvoyez `True`, sinon renvoyez `False`.

```python
from datetime import datetime

def is_weekend(d = datetime.today()):
  return d.weekday() > 4
```

```python
from datetime import date

is_weekend(date(2020, 10, 25)) # True
is_weekend(date(2020, 10, 28)) # False
```
