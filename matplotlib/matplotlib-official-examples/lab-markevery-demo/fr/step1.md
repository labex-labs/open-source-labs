# Définir les points de données

Tout d'abord, nous définissons les points de données que nous utiliserons pour nos graphiques. Dans cet exemple, nous utilisons `numpy` pour générer un ensemble de valeurs x et y pour une onde sinusoïdale.

```python
import matplotlib.pyplot as plt
import numpy as np

# définir une liste de cas markevery à tracer
cases = [
    None,
    8,
    (30, 8),
    [16, 24, 32],
    [0, -1],
    slice(100, 200, 3),
    0.1,
    0.4,
    (0.2, 0.4)
]

# points de données
delta = 0.11
x = np.linspace(0, 10 - 2 * delta, 200) + delta
y = np.sin(x) + 1.0 + delta
```
