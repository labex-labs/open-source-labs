# Crear un objeto de temporizador

Crea un nuevo objeto de temporizador. Establece el intervalo en 100 milisegundos (1000 es el valor predeterminado) y indica al temporizador qué función debe llamarse.

```python
timer = fig.canvas.new_timer(interval=100)
timer.add_callback(update_title, ax)
```
