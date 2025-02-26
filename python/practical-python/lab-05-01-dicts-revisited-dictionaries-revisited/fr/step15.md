# Le motif "Mixin"

Le motif _Mixin_ est une classe avec un fragment de code.

```python
class Loud:
    def noise(self):
        return super().noise().upper()
```

Cette classe ne peut pas être utilisée isolément. Elle est combinée avec d'autres classes via l'héritage.

```python
class LoudDog(Loud, Dog):
    pass

class LoudBike(Loud, Bike):
    pass
```

Miracle, la capacité à être bruyant a maintenant été implémentée une seule fois et réutilisée dans deux classes complètement non liées. Ce genre de tour de passe-passe est l'une des principales utilisations de l'héritage multiple en Python.
