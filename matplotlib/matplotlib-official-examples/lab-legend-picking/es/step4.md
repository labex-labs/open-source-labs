# Crear líneas y leyenda

Crearemos dos líneas y una leyenda utilizando Matplotlib.

```python
line1, = ax.plot(t, y1, lw=2, label='1 Hz')
line2, = ax.plot(t, y2, lw=2, label='2 Hz')
leg = ax.legend(fancybox=True, shadow=True)
```
