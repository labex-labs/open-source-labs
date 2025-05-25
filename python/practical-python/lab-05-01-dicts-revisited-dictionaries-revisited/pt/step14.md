# Uma Reutilização de Código Estranha (Envolvendo Herança Múltipla)

Considere dois objetos completamente não relacionados:

```python
class Dog:
    def noise(self):
        return 'Bark'

    def chase(self):
        return 'Chasing!'

class LoudDog(Dog):
    def noise(self):
        # Code commonality with LoudBike (below)
        return super().noise().upper()
```

E

```python
class Bike:
    def noise(self):
        return 'On Your Left'

    def pedal(self):
        return 'Pedaling!'

class LoudBike(Bike):
    def noise(self):
        # Code commonality with LoudDog (above)
        return super().noise().upper()
```

Há uma similaridade de código na implementação de `LoudDog.noise()` e `LoudBike.noise()`. Na verdade, o código é exatamente o mesmo. Naturalmente, código como esse está fadado a atrair engenheiros de software.
