# Por que `super()`

Sempre use `super()` ao substituir métodos.

```python
class Loud:
    def noise(self):
        return super().noise().upper()
```

`super()` delega para a _próxima classe_ na MRO (Method Resolution Order - Ordem de Resolução de Métodos).

A parte complicada é que você não sabe qual é essa classe. Especialmente, você não sabe qual é se a herança múltipla estiver sendo usada.
