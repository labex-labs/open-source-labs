# Date au format ISO

## Problème

Écrivez une fonction `to_iso_date(d)` qui prend un objet `datetime.datetime` en argument et renvoie une chaîne représentant la date au format ISO-8601. La fonction devrait utiliser la méthode `datetime.datetime.isoformat()` pour convertir la date en sa représentation ISO-8601.

## Exemple

```python
from datetime import datetime

to_iso_date(datetime(2020, 10, 25)) # "2020-10-25T00:00:00"
```
