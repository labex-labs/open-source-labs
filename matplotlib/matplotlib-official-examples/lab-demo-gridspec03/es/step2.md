# Generar subtramas con `GridSpec`

En este paso, usaremos `GridSpec` para generar subtramas. Crearemos una figura con 2 filas y 2 columnas. También especificaremos `width_ratios` y `height_ratios` para controlar los tamaños relativos de las subtramas.

```python
fig = plt.figure()
gs = GridSpec(2, 2, width_ratios=[1, 2], height_ratios=[4, 1])
ax1 = fig.add_subplot(gs[0])
ax2 = fig.add_subplot(gs[1])
ax3 = fig.add_subplot(gs[2])
ax4 = fig.add_subplot(gs[3])
```
