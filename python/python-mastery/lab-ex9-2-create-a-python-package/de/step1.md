# Ein Paket erstellen

In früheren Übungen haben Sie die folgenden Dateien erstellt, die mit typengeprüften Strukturen, Datenlesen und Tabellen erstellt wurden:

- `structure.py`
- `validate.py`
- `reader.py`
- `tableformat.py`

Ihre Aufgabe ist es, alle diese Dateien zu nehmen und in ein Paket namens `structly` zu verschieben. Um das zu tun, folgen Sie diesen Schritten:

- Erstellen Sie ein Verzeichnis namens `structly`
- Erstellen Sie eine leere Datei `__init__.py` und legen Sie sie im `structly`-Verzeichnis ab
- Verschieben Sie die Dateien `structure.py`, `validate.py`, `reader.py` und `tableformat.py` in das `structly`-Verzeichnis.
- Beheben Sie alle Importanweisungen zwischen Modulen (insbesondere hängt das `structure`-Modul von `validate` ab).

Sobald Sie das getan haben, modifizieren Sie das `stock.py`-Programm so, dass es genau so aussieht und funktioniert:

```python
# stock.py

from structly.structure import Structure

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
    from structly.reader import read_csv_as_instances
    from structly.tableformat import create_formatter, print_table
    portfolio = read_csv_as_instances('portfolio.csv', Stock)
    formatter = create_formatter('text')
    print_table(portfolio, ['name','shares','price'], formatter)
```
