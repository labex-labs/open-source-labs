# Crear la animación

Ahora crearemos la animación usando la función `FuncAnimation` de Matplotlib.

```python
ani = animation.FuncAnimation(
    fig, animate, len(y), interval=dt*1000, blit=True)
plt.show()
```
