# Date est un week-end

## Problème

Écrivez une fonction `is_weekend(d)` qui prend un objet date en entrée et renvoie `True` si la date donnée est un week-end, et `False` sinon. Si aucun argument n'est fourni, la fonction devrait utiliser la date actuelle.

Pour résoudre ce problème, vous pouvez suivre ces étapes :

1. Utilisez la méthode `datetime.datetime.weekday()` pour obtenir le jour de la semaine sous forme d'un entier.
2. Vérifiez si le jour de la semaine est supérieur à `4`. Si c'est le cas, renvoyez `True`, sinon renvoyez `False`.

## Exemple

```python
from datetime import date

assert is_weekend(date(2022, 1, 1)) == True
assert is_weekend(date(2022, 1, 3)) == False
assert is_weekend() == False # la date actuelle n'est pas un week-end
```
