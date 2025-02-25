# Crear la animación

El séptimo paso es crear el objeto de animación utilizando la función `FuncAnimation`. Le pasamos el objeto de figura, la función de animación, el intervalo entre fotogramas en milisegundos, el número de fotogramas y un retraso antes de repetir la animación.

```python
ani = animation.FuncAnimation(
    fig,
    animate,
    interval=50,
    blit=False,  # blitting no se puede utilizar con artistas de Figure
    frames=x,
    repeat_delay=100,
)
```
