# Jours à partir d'aujourd'hui

Écrivez une fonction `days_from_now(n)` qui prend un entier `n` en entrée et renvoie la date de `n` jours à partir d'aujourd'hui.

Pour résoudre ce problème, vous pouvez suivre ces étapes :

1. Importez le module `datetime`.
2. Utilisez la méthode `date.today()` pour obtenir la date actuelle.
3. Utilisez la méthode `timedelta` pour ajouter `n` jours à la date actuelle.
4. Retournez la nouvelle date.

```python
from datetime import timedelta, date

def days_from_now(n):
  return date.today() + timedelta(n)
```

```python
days_from_now(5) # date(2020, 11, 02)
```
