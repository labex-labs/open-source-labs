# Crear la segunda gráfica

A continuación, crearemos la segunda gráfica. Usaremos `subplot` nuevamente, pero esta vez estableceremos el atributo `sharex` en la primera gráfica (`ax1`). Esto asegura que la segunda gráfica compartirá el mismo eje x que la primera gráfica.

```python
ax2 = plt.subplot(212, sharex=ax1)
ax2.plot(t, np.sin(4*np.pi*t))
```
