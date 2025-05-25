# Definir os Pontos de Dados

Primeiramente, definimos os pontos de dados que usaremos para nossos gráficos. Neste exemplo, usamos `numpy` para gerar um conjunto de valores x e y para uma onda senoidal.

```python
import matplotlib.pyplot as plt
import numpy as np

# define a list of markevery cases to plot
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

# data points
delta = 0.11
x = np.linspace(0, 10 - 2 * delta, 200) + delta
y = np.sin(x) + 1.0 + delta
```
