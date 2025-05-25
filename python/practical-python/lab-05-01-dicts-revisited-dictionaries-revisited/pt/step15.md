# O Padrão "Mixin"

O padrão _Mixin_ é uma classe com um fragmento de código.

```python
class Loud:
    def noise(self):
        return super().noise().upper()
```

Esta classe não é utilizável isoladamente. Ela se mistura com outras classes via herança.

```python
class LoudDog(Loud, Dog):
    pass

class LoudBike(Loud, Bike):
    pass
```

Milagrosamente, a intensidade agora foi implementada apenas uma vez e reutilizada em duas classes completamente não relacionadas. Esse tipo de truque é um dos principais usos da herança múltipla em Python.
