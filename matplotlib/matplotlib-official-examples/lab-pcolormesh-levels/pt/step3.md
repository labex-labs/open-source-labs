# Coordenadas Centradas

Frequentemente, um usuário deseja passar _X_ e _Y_ com os mesmos tamanhos que _Z_ para `.axes.Axes.pcolormesh`. Isso também é permitido se `shading='auto'` for passado (configuração padrão por :rc:`pcolor.shading`). Antes do Matplotlib 3.3, `shading='flat'` descartaria a última coluna e linha de _Z_, mas agora gera um erro. Se isso é realmente o que você deseja, então simplesmente descarte a última linha e coluna de Z manualmente:

```python
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(19680801)
Z = np.random.rand(6, 10)
x = np.arange(10)  # len = 10
y = np.arange(6)  # len = 6
X, Y = np.meshgrid(x, y)

fig, axs = plt.subplots(2, 1, sharex=True, sharey=True)
axs[0].pcolormesh(X, Y, Z, vmin=np.min(Z), vmax=np.max(Z), shading='auto')
axs[0].set_title("shading='auto' = 'nearest'")
axs[1].pcolormesh(X, Y, Z[:-1, :-1], vmin=np.min(Z), vmax=np.max(Z),
                  shading='flat')
axs[1].set_title("shading='flat'")
```
