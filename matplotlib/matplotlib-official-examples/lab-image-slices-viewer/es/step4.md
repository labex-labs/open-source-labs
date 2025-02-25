# Crear la gráfica y conectar el evento de desplazamiento

Vamos a crear la gráfica utilizando la función `subplots` de Matplotlib y pasarle el objeto `IndexTracker` creado. Luego, conectaremos el evento de desplazamiento a la superficie del gráfico utilizando `mpl_connect`.

```python
fig, ax = plt.subplots()
tracker = IndexTracker(ax, X)

fig.canvas.mpl_connect('scroll_event', tracker.on_scroll)
plt.show()
```
