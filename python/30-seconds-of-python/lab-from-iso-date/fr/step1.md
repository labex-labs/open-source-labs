# Convertir une date au format ISO

Écrivez une fonction `from_iso_date(d)` qui prend une chaîne de caractères `d` représentant une date au format ISO-8601 et renvoie un objet `datetime.datetime` représentant la même date et heure.

```python
from datetime import datetime

def from_iso_date(d):
  return datetime.fromisoformat(d)
```

```python
from_iso_date('2020-10-28T12:30:59.000000') # 2020-10-28 12:30:59
```
