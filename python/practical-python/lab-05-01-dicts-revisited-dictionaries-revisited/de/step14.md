# Ein sonderbarer Code-Wiederverwendungseffekt (mit Mehrfachvererbung)

Betrachten Sie zwei völlig unverbundene Objekte:

```python
class Dog:
    def noise(self):
        return 'Bark'

    def chase(self):
        return 'Chasing!'

class LoudDog(Dog):
    def noise(self):
        # Code-Ähnlichkeit mit LoudBike (siehe unten)
        return super().noise().upper()
```

Und

```python
class Bike:
    def noise(self):
        return 'On Your Left'

    def pedal(self):
        return 'Pedaling!'

class LoudBike(Bike):
    def noise(self):
        # Code-Ähnlichkeit mit LoudDog (siehe oben)
        return super().noise().upper()
```

Es gibt eine Code-Ähnlichkeit in der Implementierung von `LoudDog.noise()` und `LoudBike.noise()`. Tatsächlich ist der Code genau derselbe. Natürlich wird ein solcher Code sicherlich Softwareingenieure ansprechen.
