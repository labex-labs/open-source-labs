# Vérifiez si une date est un jour de semaine

Écrivez une fonction Python appelée `is_weekday()` qui prend une date en entrée et renvoie `True` si c'est un jour de semaine, et `False` si c'est un week-end. Si aucune date n'est fournie, la fonction devrait utiliser la date actuelle.

Pour résoudre ce problème, vous pouvez suivre ces étapes :

1. Importez le module `datetime`.
2. Définissez une fonction appelée `is_weekday()` qui prend une date en entrée. Si aucune date n'est fournie, utilisez la date actuelle.
3. Utilisez la méthode `weekday()` du module `datetime` pour obtenir le jour de la semaine sous forme d'un entier. La méthode `weekday()` renvoie un entier compris entre 0 (lundi) et 6 (dimanche).
4. Vérifiez si le jour de la semaine est inférieur ou égal à 4. Si c'est le cas, renvoyez `True`, sinon renvoyez `False`.

```python
from datetime import datetime

def is_weekday(d = datetime.today()):
  return d.weekday() <= 4
```

```python
from datetime import date

is_weekday(date(2020, 10, 25)) # False
is_weekday(date(2020, 10, 28)) # True
```
