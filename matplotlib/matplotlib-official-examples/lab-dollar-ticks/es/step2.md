# Crear el Gráfico

A continuación, creemos un gráfico simple con el que trabajar. Utilizaremos NumPy para generar algunos datos aleatorios para graficar.

```python
import numpy as np

# Generate random data
np.random.seed(19680801)
data = 100 * np.random.rand(20)

# Create the plot
fig, ax = plt.subplots()
ax.plot(data)
```
