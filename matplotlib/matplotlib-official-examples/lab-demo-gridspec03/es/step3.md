# Controlar el espaciado alrededor y entre las subtramas

En este paso, usaremos `GridSpec` para controlar el espaciado alrededor y entre las subtramas. Crearemos una figura con 2 gridspecs, cada uno con 3 filas y 3 columnas. Especificaremos los parámetros `left`, `right`, `bottom`, `top`, `wspace` y `hspace` para controlar el espaciado.

```python
fig = plt.figure()
gs1 = GridSpec(3, 3, left=0.05, right=0.48, wspace=0.05)
ax1 = fig.add_subplot(gs1[:-1, :])
ax2 = fig.add_subplot(gs1[-1, :-1])
ax3 = fig.add_subplot(gs1[-1, -1])

gs2 = GridSpec(3, 3, left=0.55, right=0.98, hspace=0.05)
ax4 = fig.add_subplot(gs2[:, :-1])
ax5 = fig.add_subplot(gs2[:-1, -1])
ax6 = fig.add_subplot(gs2[-1, -1])
```
