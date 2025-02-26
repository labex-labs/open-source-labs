# Contrôle des symboles exportés

Modifiez tous les sous-modules du package `structly` de manière à définir explicitement une variable `__all__` qui exporte les symboles sélectionnés. Plus précisément :

- `structure.py` devrait exporter `Structure`
- `reader.py` devrait exporter toutes les diverses fonctions `read_csv_as_*()`
- `tableformat.py` exporte `create_formatter()` et `print_table()`

Maintenant, dans le fichier `__init__.py`, regroupez tous les sous-modules comme ceci :

```python
# structly/__init__.py

from.structure import *
from.reader import *
from.tableformat import *
```

Une fois que vous avez fait cela, vous devriez être en mesure d'importer tout à partir d'un seul module logique :

```python
# stock.py

from structly import Structure

class Stock(Structure):
    name = String()
    shares = PositiveInteger()
    price = PositiveFloat()

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, nshares: PositiveInteger):
        self.shares -= nshares

if __name__ == '__main__':
    from structly import read_csv_as_instances, create_formatter, print_table
    portfolio = read_csv_as_instances('portfolio.csv', Stock)
    formatter = create_formatter('text')
    print_table(portfolio, ['name','shares','price'], formatter)
```
