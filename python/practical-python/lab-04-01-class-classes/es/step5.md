# Métodos de instancia

Los métodos de instancia son funciones aplicadas a las instancias de un objeto.

```python
class Player:
  ...
    # `move` es un método
    def move(self, dx, dy):
        self.x += dx
        self.y += dy
```

El objeto mismo siempre se pasa como primer argumento.

```python
>>> a.move(1, 2)

# hace coincidir `a` con `self`
# hace coincidir `1` con `dx`
# hace coincidir `2` con `dy`
def move(self, dx, dy):
```

Por convención, la instancia se llama `self`. Sin embargo, el nombre real utilizado no es importante. El objeto siempre se pasa como primer argumento. Es simplemente un estilo de programación de Python llamar a este argumento `self`.
