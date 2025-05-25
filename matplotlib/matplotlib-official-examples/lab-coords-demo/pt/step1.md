# Criando um Gráfico de Onda Senoidal

Primeiramente, precisamos criar um gráfico de onda senoidal usando as bibliotecas numpy e matplotlib.

```python
import matplotlib.pyplot as plt
import numpy as np

t = np.arange(0.0, 1.0, 0.01)
s = np.sin(2 * np.pi * t)
fig, ax = plt.subplots()
ax.plot(t, s)
```
