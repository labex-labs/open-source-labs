# Il y a n jours

Votre tâche est d'écrire une fonction appelée `days_ago(n)` qui prend un entier `n` en argument et renvoie la date il y a `n` jours avant aujourd'hui.

Pour résoudre ce problème, vous devez utiliser la classe `date` du module `datetime` pour obtenir la date actuelle et la classe `timedelta` pour soustraire `n` jours à la date actuelle.

```python
from datetime import timedelta, date

def days_ago(n):
  return date.today() - timedelta(n)
```

```python
days_ago(5) # date(2020, 10, 23)
```
