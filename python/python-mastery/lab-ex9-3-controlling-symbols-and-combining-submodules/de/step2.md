# Kontrolle über exportierte Symbole

Ändern Sie alle Untermodule im `structly`-Paket so, dass sie explizit eine `__all__`-Variable definieren, die ausgewählte Symbole exportiert. Genauer gesagt:

- `structure.py` sollte `Structure` exportieren
- `reader.py` sollte alle verschiedenen `read_csv_as_*()`-Funktionen exportieren
- `tableformat.py` exportiert `create_formatter()` und `print_table()`

Nun vereinigen Sie alle Untermodule in der `__init__.py`-Datei wie folgt:

```python
# structly/__init__.py

from.structure import *
from.reader import *
from.tableformat import *
```

Wenn Sie dies getan haben, sollten Sie alles aus einem einzelnen logischen Modul importieren können:

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
