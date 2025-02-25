# Crear la figura y los ejes

En este paso, creará la figura y los ejes para la gráfica. También ajustará la posición de los ejes para dejar espacio para los deslizadores.

```python
fig, ax = plt.subplots()
fig.subplots_adjust(bottom=0.25)
l, = ax.plot(t, s, lw=2)

ax_freq = fig.add_axes([0.25, 0.1, 0.65, 0.03])
ax_amp = fig.add_axes([0.25, 0.15, 0.65, 0.03])
```
