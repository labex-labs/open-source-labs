# Beispiel: Eindeutige-Mehrdeutige Zuordnungen

Problem: Sie möchten einen Schlüssel zu mehreren Werten zuordnen.

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

Wie im vorherigen Beispiel sollte der Schlüssel `IBM` stattdessen zwei verschiedene Tupel haben.

Lösung: Verwenden Sie ein `defaultdict`.

```python
from collections import defaultdict
holdings = defaultdict(list)
for name, shares, price in portfolio:
    holdings[name].append((shares, price))
holdings['IBM'] # [ (50, 91.1), (100, 45.23) ]
```

Das `defaultdict` stellt sicher, dass Sie jedes Mal, wenn Sie auf einen Schlüssel zugreifen, einen Standardwert erhalten.
