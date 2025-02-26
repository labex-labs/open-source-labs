# Défi : élimination des noms

Modifiez le code de `typedproperty.py` de sorte que les noms d'attributs ne soient plus nécessaires :

```python
from typedproperty import String, Integer, Float

class Stock:
    name = String()
    shares = Integer()
    price = Float()
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
```

Indice : Pour ce faire, rappelez-vous la méthode `__set_name__()` des objets descripteurs qui est appelée lorsqu'un descripteur est placé dans une définition de classe.
