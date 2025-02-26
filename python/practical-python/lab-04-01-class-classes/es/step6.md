# Alcance de clase

Las clases no definen un ámbito de nombres.

```python
class Player:
 ...
    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def left(self, amt):
        move(-amt, 0)       # NO. Llama a una función global `move`
        self.move(-amt, 0)  # SI. Llama al método `move` de arriba.
```

Si quieres operar sobre una instancia, siempre la referenciar explícitamente (por ejemplo, `self`).

A partir de este conjunto de ejercicios, comenzamos a realizar una serie de cambios en el código existente de secciones anteriores. Es fundamental que tengas una versión funcional del Ejercicio 3.18 para comenzar. Si no la tienes, por favor trabaja a partir del código de solución que se encuentra en el directorio `Solutions/3_18`. Está bien copiarlo.
