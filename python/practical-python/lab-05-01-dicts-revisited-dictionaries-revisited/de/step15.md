# Das "Mixin"-Muster

Das _Mixin_-Muster ist eine Klasse mit einem Codefragment.

```python
class Loud:
    def noise(self):
        return super().noise().upper()
```

Diese Klasse kann nicht in isolation verwendet werden. Sie mischt sich mit anderen Klassen über Vererbung.

```python
class LoudDog(Loud, Dog):
    pass

class LoudBike(Loud, Bike):
    pass
```

Wunderbarerweise wurde die Lautstärke jetzt nur einmal implementiert und in zwei völlig unverbundenen Klassen wiederverwendet. Solch ein Trick ist eine der primären Anwendungen der Mehrfachvererbung in Python.
