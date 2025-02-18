# Configurar la gráfica

Creamos un nuevo objeto figura y eje y inicializamos la clase Scope. Luego, pasamos las funciones de actualización y emisor al método FuncAnimation para crear la animación.

```python
fig, ax = plt.subplots()
scope = Scope(ax)

ani = animation.FuncAnimation(fig, scope.update, emitter, interval=50,
                              blit=True, save_count=100)

plt.show()
```
