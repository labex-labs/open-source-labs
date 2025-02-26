# El Patrón "Mixin"

El patrón _Mixin_ es una clase con un fragmento de código.

```python
class Loud:
    def noise(self):
        return super().noise().upper()
```

Esta clase no es usable por sí sola. Se mezcla con otras clases a través de la herencia.

```python
class LoudDog(Loud, Dog):
    pass

class LoudBike(Loud, Bike):
    pass
```

Míraculosamente, la alta volumen se implementó solo una vez y se reutilizó en dos clases completamente no relacionadas. Este tipo de truco es uno de los usos principales de la herencia múltiple en Python.
