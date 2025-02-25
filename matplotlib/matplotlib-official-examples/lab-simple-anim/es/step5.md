# Crear el objeto de animación

Ahora podemos crear el objeto de animación utilizando la función `FuncAnimation()`. Pasaremos el objeto de figura, la función de animación, el intervalo de actualización y el número de fotogramas que se guardarán.

```python
ani = animation.FuncAnimation(
    fig, animate, interval=20, blit=True, save_count=50)
```
