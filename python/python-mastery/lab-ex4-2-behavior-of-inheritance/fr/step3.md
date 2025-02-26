# Utilisation de vos validateurs

Vos validateurs peuvent être utilisés pour ajouter des vérifications de valeurs à des fonctions et des classes. Par exemple, peut-être que les validateurs pourraient être utilisés dans les propriétés de `Stock` :

```python
class Stock:
  ...
    @property
    def shares(self):
        return self._shares

    @shares.setter
    def shares(self, value):
        self._shares = PositiveInteger.check(value)
  ...
```

Copiez la classe `Stock` de `stock.py` et modifiez-la pour utiliser les validateurs dans le code des propriétés pour `shares` et `price`.
