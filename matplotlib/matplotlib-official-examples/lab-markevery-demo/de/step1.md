# Definieren der Datenpunkte

Zunächst definieren wir die Datenpunkte, die wir für unsere Graphen verwenden werden. In diesem Beispiel verwenden wir `numpy`, um eine Reihe von x- und y-Werten für eine Sinuswelle zu generieren.

```python
import matplotlib.pyplot as plt
import numpy as np

# definieren einer Liste von markevery-Fällen, die geplottet werden sollen
fälle = [
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

# Datenpunkte
delta = 0.11
x = np.linspace(0, 10 - 2 * delta, 200) + delta
y = np.sin(x) + 1.0 + delta
```
