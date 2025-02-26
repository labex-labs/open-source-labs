# Pourquoi utiliser `super()`

Utilisez toujours `super()` lorsqu'il s'agit de surcharger des méthodes.

```python
class Loud:
    def noise(self):
        return super().noise().upper()
```

`super()` délègue à la _classe suivante_ dans l'ordre MRO.

Le point délicat est que vous ne savez pas laquelle c'est. Vous ne savez surtout pas laquelle c'est si l'héritage multiple est utilisé.
