# Crear la animación

Ahora crearemos la animación utilizando el método `ArtistAnimation`. Pasaremos el objeto de figura, la lista `ims`, el intervalo entre los fotogramas y el retraso de repetición.

```python
ani = animation.ArtistAnimation(fig, ims, interval=50, blit=True, repeat_delay=1000)
```
