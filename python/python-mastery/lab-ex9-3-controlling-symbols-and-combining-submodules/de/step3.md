# Exportieren von allem

In der `structly/__init__.py` definieren Sie eine `__all__`-Variable, die alle exportierten Symbole enthält. Nachdem Sie dies getan haben, sollten Sie die `stock.py`-Datei weiter vereinfachen können:

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

Nebenbei bemerkt, wird die Verwendung der `from module import *`-Anweisung im Python-Community im Allgemeinen nicht gerne gesehen - insbesondere wenn Sie nicht wissen, was Sie tun. Allerdings gibt es Situationen, in denen es oft Sinn macht. Beispielsweise kann es nützlich sein, wenn ein Paket eine große Anzahl von allgemein verwendeten Symbolen oder Konstanten definiert.
