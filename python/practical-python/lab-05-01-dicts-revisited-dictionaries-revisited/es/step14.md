# Un Uso Extraño de Reutilización de Código (Involucrando Herencia Múltiple)

Considera dos objetos completamente no relacionados:

```python
class Dog:
    def noise(self):
        return 'Bark'

    def chase(self):
        return 'Chasing!'

class LoudDog(Dog):
    def noise(self):
        # Código en común con LoudBike (abajo)
        return super().noise().upper()
```

Y

```python
class Bike:
    def noise(self):
        return 'On Your Left'

    def pedal(self):
        return 'Pedaling!'

class LoudBike(Bike):
    def noise(self):
        # Código en común con LoudDog (arriba)
        return super().noise().upper()
```

Hay un código en común en la implementación de `LoudDog.noise()` y `LoudBike.noise()`. De hecho, el código es exactamente el mismo. Naturalmente, código como ese está destinado a atraer a los ingenieros de software.
