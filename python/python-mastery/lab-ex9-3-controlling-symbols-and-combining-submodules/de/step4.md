# Modulunterteilung

Die Datei `structly/tableformat.py` enthält Code zum Erstellen von Tabellen in verschiedenen Formaten. Genauer gesagt:

- Eine Basisklasse `TableFormatter`.
- Eine Klasse `TextTableFormatter`.
- Eine Klasse `CSVTableFormatter`.
- Eine Klasse `HTMLTableFormatter`.

Anstatt alle diese Klassen in einer einzigen `.py`-Datei zu haben, wäre es vielleicht sinnvoll, jede konkrete Formatierung in ihre eigene Datei zu verschieben. Um dies zu tun, werden wir die `tableformat.py`-Datei in Teile aufteilen. Befolgen Sie diese Anweisungen genau:

Zunächst entfernen Sie das Verzeichnis `structly/__pycache__`.

    % cd structly
    % rm -rf __pycache__

Als Nächstes erstellen Sie das Verzeichnis `structly/tableformat`. Dieses Verzeichnis muss genau den gleichen Namen wie das Modul haben, das es ersetzt (`tableformat.py`).

```bash
mkdir tableformat
```

Bewegen Sie die ursprüngliche `tableformat.py`-Datei in das neue `tableformat`-Verzeichnis und benennen Sie sie in `formatter.py` um.

```bash
mv tableformat.py tableformat/formatter.py
```

Im `tableformat`-Verzeichnis teilen Sie den `tableformat.py`-Code in die folgenden Dateien und Verzeichnisse auf:

- `formatter.py` - Enthält die `TableFormatter`-Basisklasse, Mixins und verschiedene Funktionen.
- `formats/text.py` - Enthält die `TextTableFormatter`-Klasse.
- `formats/csv.py` - Enthält die `CSVTableFormatter`-Klasse.
- `formats/html.py` - Enthält die `HTMLTableFormatter`-Klasse.

Fügen Sie eine `__init__.py`-Datei in das `tableformat/` und `tableformat/formats`-Verzeichnis hinzu. Lassen Sie die `tableformat/__init__.py` die gleichen Symbole exportieren, die die ursprüngliche `tableformat.py`-Datei exportierte.

Nachdem Sie alle diese Änderungen vorgenommen haben, sollten Sie eine Paketstruktur haben, die wie folgt aussieht:

    structly/
          __init__.py
          validate.py
          reader.py
          structure.py
          tableformat/
               __init__.py
               formatter.py
               formats/
                   __init__.py
                   text.py
                   csv.py
                   html.py

Für die Benutzer sollte alles genauso funktionieren wie zuvor. Beispielsweise sollte Ihre vorherige `stock.py`-Datei funktionieren:

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

    def sell(self, nshares):
        self.shares -= nshares

if __name__ == '__main__':
    portfolio = read_csv_as_instances('portfolio.csv', Stock)
    formatter = create_formatter('text')
    print_table(portfolio, ['name','shares','price'], formatter)
```
