# Criando um Gráfico

Para criar um gráfico, primeiro precisamos definir os dados que queremos plotar. Neste exemplo, usaremos a biblioteca `numpy` para gerar alguns dados de amostra.

```python
import numpy as np

x = np.linspace(0, 10, 1000)
y = np.sin(x)
```

Em seguida, criamos uma nova figura e eixos usando `plt.subplots()`. Definiremos os limites x e y do gráfico e, em seguida, plotaremos os dados usando `plot()`.

```python
fig, ax = plt.subplots()
ax.set_xlim([0, 10])
ax.set_ylim([-1.2, 1.2])
ax.plot(x, y)
```
