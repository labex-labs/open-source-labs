# Graficando los datos

Graficaremos los datos aleatorios generados en el Paso 2 utilizando la función `plot()` dos veces. La primera gráfica tendrá un valor de alfa de 0.2 y la segunda gráfica tendrá un valor de alfa de 1.0 y una ruta de recorte establecida en el parche de círculo amarillo.

```python
ax.plot(x, y, alpha=0.2)
line, = ax.plot(x, y, alpha=1.0, clip_path=circ)
ax.set_title("Left click and drag to move looking glass")
```
