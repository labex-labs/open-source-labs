# Creando subgráficos

Ahora crearemos una cuadrícula de subgráficos de 2x2 utilizando la función `subplots`. Esto nos dará cuatro gráficos para visualizar el patrón de esparcidad de la matriz.

```python
fig, axs = plt.subplots(2, 2)
ax1 = axs[0, 0]
ax2 = axs[0, 1]
ax3 = axs[1, 0]
ax4 = axs[1, 1]
```
