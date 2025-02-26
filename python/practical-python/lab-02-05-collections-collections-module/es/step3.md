# Ejemplo: Mapeos de Uno a Varios

Problema: Quieres mapear una clave a múltiples valores.

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

Como en el ejemplo anterior, la clave `IBM` debería tener dos tuplas diferentes en lugar de eso.

Solución: Utiliza un `defaultdict`.

```python
from collections import defaultdict
holdings = defaultdict(list)
for name, shares, price in portfolio:
    holdings[name].append((shares, price))
holdings['IBM'] # [ (50, 91.1), (100, 45.23) ]
```

El `defaultdict` asegura que cada vez que accedes a una clave obtienes un valor predeterminado.
