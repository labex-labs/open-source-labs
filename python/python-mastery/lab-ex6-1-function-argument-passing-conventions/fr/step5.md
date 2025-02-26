# Recommencer

Créez un nouveau fichier `stock.py` (ou supprimez tout votre code précédent). Commencez à nouveau en définissant `Stock` comme suit :

```python
# stock.py

from structure import Structure

class Stock(Structure):
    _fields = ('name','shares', 'price')

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, nshares):
        self.shares -= nshares
```

Une fois que vous avez fait cela, exécutez vos tests unitaires `teststock.py`. Vous devriez obtenir beaucoup d'échecs, mais au moins quelques-uns des tests devraient réussir.
