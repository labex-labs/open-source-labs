# Criar uma Classe de Unidade Personalizada

Nesta etapa, criaremos uma classe de unidade personalizada - `Foo`. Esta classe suportará conversão e diferentes formatações de ticks dependendo da "unidade". Aqui, a "unidade" é apenas um fator de conversão escalar.

```python
class Foo:
    def __init__(self, val, unit=1.0):
        self.unit = unit
        self._val = val * unit

    def value(self, unit):
        if unit is None:
            unit = self.unit
        return self._val / unit
```
