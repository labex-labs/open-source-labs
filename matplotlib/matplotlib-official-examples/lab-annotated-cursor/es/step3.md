# Crear la clase AnnotatedCursor

Creamos una nueva clase `AnnotatedCursor` que hereda de `matplotlib.widgets.Cursor` y demuestra la creación de nuevos widgets y sus devoluciones de llamada de eventos. La clase `AnnotatedCursor` se utiliza para crear un cursor de cruz con un texto que muestra las coordenadas actuales.

```python
class AnnotatedCursor(Cursor):
    """
    Un cursor de cruz como `~matplotlib.widgets.Cursor` con un texto que muestra \
    las coordenadas actuales.
  ...
    """
```
