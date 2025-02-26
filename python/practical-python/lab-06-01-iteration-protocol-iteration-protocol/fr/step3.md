# Prise en charge de l'itération

Il est utile de connaître l'itération si vous voulez l'ajouter à vos propres objets. Par exemple, pour créer un conteneur personnalisé.

```python
class Portfolio:
    def __init__(self):
        self.holdings = []

    def __iter__(self):
        return self.holdings.__iter__()
  ...

port = Portfolio()
for s in port:
  ...
```
