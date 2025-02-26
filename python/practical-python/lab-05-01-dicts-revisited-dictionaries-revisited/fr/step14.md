# Un réutilisation de code étrange (impliquant l'héritage multiple)

Considérez deux objets complètement non liés :

```python
class Dog:
    def noise(self):
        return 'Bark'

    def chase(self):
        return 'Chasing!'

class LoudDog(Dog):
    def noise(self):
        # Code commun avec LoudBike (ci-dessous)
        return super().noise().upper()
```

Et

```python
class Bike:
    def noise(self):
        return 'On Your Left'

    def pedal(self):
        return 'Pedaling!'

class LoudBike(Bike):
    def noise(self):
        # Code commun avec LoudDog (ci-dessus)
        return super().noise().upper()
```

Il y a une similitude de code dans l'implémentation de `LoudDog.noise()` et `LoudBike.noise()`. En fait, le code est exactement le même. Naturellement, un code comme celui-ci est certainement susceptible d'attirer les ingénieurs logiciels.
