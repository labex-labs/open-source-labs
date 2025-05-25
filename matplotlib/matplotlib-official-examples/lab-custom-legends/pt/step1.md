# Plotando Linhas

Nesta etapa, plotaremos um conjunto de linhas usando a biblioteca Matplotlib. Primeiro, criamos alguns dados aleatórios usando NumPy. Em seguida, definimos o ciclo de cores usando a função `cycler` para especificar o mapa de cores. Finalmente, plotamos os dados usando a função `plot` e chamamos `legend()` para gerar a legenda.

```python
import matplotlib.pyplot as plt
import numpy as np

# Set random state for reproducibility
np.random.seed(19680801)

# Create random data
N = 10
data = (np.geomspace(1, 10, 100) + np.random.randn(N, 100)).T

# Set color cycle
cmap = plt.cm.coolwarm
plt.rcParams['axes.prop_cycle'] = cycler(color=cmap(np.linspace(0, 1, N)))

# Plot data and generate legend
fig, ax = plt.subplots()
lines = ax.plot(data)
ax.legend()
```
