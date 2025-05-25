# Gráfico de dispersão sem o modo autolimit_mode round_numbers

Nesta etapa, criaremos um gráfico de dispersão sem o modo autolimit_mode round_numbers e observaremos o comportamento da auto-posição de ticks.

```python
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(19680801)

fig, ax = plt.subplots()
dots = np.linspace(0.3, 1.2, 10)
X, Y = np.meshgrid(dots, dots)
x, y = X.ravel(), Y.ravel()
ax.scatter(x, y, c=x+y)
plt.show()
```
