# ¿Por qué `super()`?

Siempre utiliza `super()` cuando sobrescribes métodos.

```python
class Loud:
    def noise(self):
        return super().noise().upper()
```

`super()` delega a la _siguiente clase_ en el MRO.

Lo complicado es que no sabes cuál es. En especial, no lo sabes si se está utilizando herencia múltiple.
