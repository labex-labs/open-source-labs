# Conectar el evento a la función

Ahora, conectamos el evento de presión del botón en la primera ventana a la función on_press que acabamos de definir.

```python
figsrc.canvas.mpl_connect('button_press_event', on_press)
```
