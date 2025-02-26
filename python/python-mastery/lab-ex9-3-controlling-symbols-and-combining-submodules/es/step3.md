# Exportando Todo

En `structly/__init__.py`, define una variable `__all__` que contenga todos los símbolos exportados. Una vez que hayas hecho esto, deberías poder simplificar aún más el archivo `stock.py`:

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

Por cierto, el uso de la declaración `from module import *` generalmente no está bien visto en la comunidad de Python, especialmente si no estás seguro de lo que estás haciendo. Dicho esto, hay situaciones en las que a menudo tiene sentido. Por ejemplo, si un paquete define una gran cantidad de símbolos o constantes comúnmente utilizados, puede resultar útil utilizarlos.
