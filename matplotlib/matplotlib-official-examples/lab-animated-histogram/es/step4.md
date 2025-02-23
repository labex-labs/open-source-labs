# Crear función de animación

Necesitamos crear una función `animate` que genere nuevos datos aleatorios y actualice las alturas de los rectángulos.

```python
def animate(frame_number):
    # simular la llegada de nuevos datos
    data = np.random.randn(1000)
    n, _ = np.histogram(data, HIST_BINS)
    for count, rect in zip(n, bar_container.patches):
        rect.set_height(count)
    return bar_container.patches
```
