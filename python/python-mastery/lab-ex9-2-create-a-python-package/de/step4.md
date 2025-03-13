# Aktualisieren und Testen des stock.py-Programms

Nachdem wir unser Paket erstellt und die internen Importe korrigiert haben, ist es an der Zeit, die `stock.py`-Datei zu aktualisieren, um unsere neue Paketstruktur zu nutzen. Ein Paket in Python ist eine Möglichkeit, verwandte Module zusammen zu organisieren. Es hilft, Ihre Codebasis organisiert zu halten und erleichtert die Verwaltung und Wiederverwendung von Code.

Öffnen Sie die `stock.py`-Datei im Editor:

```bash
# Click on stock.py in the file explorer or run:
code stock.py
```

Die aktuellen Importe in `stock.py` basieren auf der alten Struktur, in der alle Dateien im gleichen Verzeichnis lagen. In Python sucht Python bei einem Modulimport an bestimmten Orten nach dem Modul. In der alten Struktur konnte Python die Module leicht finden, da alle Dateien im gleichen Verzeichnis waren. Aber jetzt, mit der neuen Paketstruktur, müssen wir die Importe aktualisieren, um Python zu sagen, wo es die Module innerhalb des `structly`-Pakets finden kann.

Aktualisieren Sie die `stock.py`-Datei so, dass sie genau wie folgt aussieht:

```python
# stock.py

from structly.structure import Structure, String, PositiveInteger, PositiveFloat

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

Die wichtigsten Änderungen sind:

1. Geändert von `from structure import Structure, String, PositiveInteger, PositiveFloat` zu `from structly.structure import Structure, String, PositiveInteger, PositiveFloat`. Diese Änderung sagt Python, dass es nach dem `structure`-Modul innerhalb des `structly`-Pakets suchen soll.
2. Geändert von `from reader import read_csv_as_instances` zu `from structly.reader import read_csv_as_instances`. Ebenso leitet diese Änderung Python an, das `reader`-Modul innerhalb des `structly`-Pakets zu finden.
3. Geändert von `from tableformat import create_formatter, print_table` zu `from structly.tableformat import create_formatter, print_table`. Dies stellt sicher, dass Python das `tableformat`-Modul im `structly`-Paket findet.

Speichern Sie die Datei nach diesen Änderungen. Das Speichern der Datei ist wichtig, da es sicherstellt, dass die von Ihnen vorgenommenen Änderungen gespeichert werden und beim Ausführen des Programms verwendet werden können.

Jetzt testen wir unseren aktualisierten Code, um sicherzustellen, dass alles korrekt funktioniert:

```bash
python stock.py
```

Sie sollten die folgende Ausgabe sehen:

```
      name      shares       price
---------- ---------- ----------
      MSFT        100      51.23
       IBM         50       91.1
      AAPL         75     145.89
      ACME        125     123.45
       HPE         75       32.2
```

Wenn Sie diese Ausgabe sehen, herzlichen Glückwunsch! Sie haben erfolgreich ein Python-Paket erstellt und Ihren Code aktualisiert, um es zu nutzen. Dies bedeutet, dass Ihr Code jetzt auf eine modularere Weise organisiert ist, was die Wartung und Erweiterung in Zukunft erleichtert.
