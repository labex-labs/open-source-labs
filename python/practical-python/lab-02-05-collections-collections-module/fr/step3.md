# Exemple : Mappages un-à-plusieurs

Problème : Vous voulez mapper une clé à plusieurs valeurs.

```python
portfolio = [
    ('GOOG', 100, 490.1),
    ('IBM', 50, 91.1),
    ('CAT', 150, 83.44),
    ('IBM', 100, 45.23),
    ('GOOG', 75, 572.45),
    ('AA', 50, 23.15)
]
```

Comme dans l'exemple précédent, la clé `IBM` devrait avoir deux tuples différents.

Solution : Utiliser un `defaultdict`.

```python
from collections import defaultdict
holdings = defaultdict(list)
for name, shares, price in portfolio:
    holdings[name].append((shares, price))
holdings['IBM'] # [ (50, 91.1), (100, 45.23) ]
```

Le `defaultdict` assure que chaque fois que vous accédez à une clé, vous obtenez une valeur par défaut.
