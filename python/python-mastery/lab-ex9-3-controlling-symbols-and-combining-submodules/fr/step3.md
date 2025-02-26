# Exporter tout

Dans le fichier `structly/__init__.py`, définissez une variable `__all__` qui contient tous les symboles exportés. Une fois que vous avez fait cela, vous devriez être en mesure de simplifier encore le fichier `stock.py` :

```python
# stock.py

from structly import *

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
    portfolio = read_csv_as_instances('portfolio.csv', Stock)
    formatter = create_formatter('text')
    print_table(portfolio, ['name','shares','price'], formatter)
```

Au passage, l'utilisation de l'instruction `from module import *` est généralement déconseillée dans la communauté Python - surtout si vous n'êtes pas sûr de ce que vous faites. Cela étant dit, il existe des situations où cela peut avoir du sens. Par exemple, si un package définit un grand nombre de symboles ou de constantes couramment utilisés, il peut être utile de l'utiliser.
