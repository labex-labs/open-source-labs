# Implementierung eines konkreten Formatierers

Nachdem wir unsere abstrakte Basisklasse definiert und die Funktion `print_table()` aktualisiert haben, ist es an der Zeit, eine konkrete Formatiererklasse zu erstellen. Eine konkrete Formatiererklasse ist eine, die tatsächliche Implementierungen für die in der abstrakten Basisklasse definierten Methoden bereitstellt. In unserem Fall werden wir eine Klasse erstellen, die Daten in eine einfache Texttabelle formatieren kann.

Fügen Sie die folgende Klasse zu Ihrer `tableformat.py` - Datei hinzu. Diese Klasse wird von der abstrakten Basisklasse `TableFormatter` erben und die Methoden `headings()` und `row()` implementieren.

```python
class TextTableFormatter(TableFormatter):
    """
    Formatter that generates a plain - text table.
    """
    def headings(self, headers):
        """
        Generate plain - text table headings.
        """
        print(' '.join('%10s' % h for h in headers))
        print(('-'*10 + ' ')*len(headers))

    def row(self, rowdata):
        """
        Generate a plain - text table row.
        """
        print(' '.join('%10s' % d for d in rowdata))
```

Die Klasse `TextTableFormatter` erbt von `TableFormatter`. Das bedeutet, dass sie alle Eigenschaften und Methoden der Klasse `TableFormatter` erhält, aber auch eigene Implementierungen für die Methoden `headings()` und `row()` bereitstellt. Diese Methoden sind jeweils für die Formatierung der Tabellenüberschriften und -zeilen verantwortlich. Die Methode `headings()` gibt die Überschriften in einem schön formatierten Stil aus, gefolgt von einer Linie aus Bindestrichen, um die Überschriften von den Daten zu trennen. Die Methode `row()` formatiert jede Datenzeile auf ähnliche Weise.

Jetzt testen wir unseren neuen Formatierer. Wir verwenden die Module `stock`, `reader` und `tableformat`, um Daten aus einer CSV - Datei zu lesen und sie mit unserem neuen Formatierer auszugeben.

```python
import stock
import reader
import tableformat

portfolio = reader.read_csv_as_instances('portfolio.csv', stock.Stock)
formatter = tableformat.TextTableFormatter()
tableformat.print_table(portfolio, ['name', 'shares', 'price'], formatter)
```

Wenn Sie diesen Code ausführen, sollten Sie die gleiche Ausgabe wie zuvor sehen. Dies liegt daran, dass unser neuer Formatierer so konzipiert ist, dass er die gleiche einfache Texttabelle wie die ursprüngliche Funktion `print_table()` erzeugt.

```
      name     shares      price
---------- ---------- ----------
        AA        100       32.2
       IBM         50       91.1
       CAT        150      83.44
      MSFT        200      51.23
        GE         95      40.37
      MSFT         50       65.1
       IBM        100      70.44
```

Diese Ausgabe bestätigt, dass unser `TextTableFormatter` korrekt funktioniert. Der Vorteil dieses Ansatzes besteht darin, dass wir unseren Code modularer und erweiterbarer gemacht haben. Indem wir die Formatierungslogik in eine separate Klassenhierarchie aufteilen, können wir leicht neue Ausgabeformate hinzufügen. Alles, was wir tun müssen, ist, neue Unterklassen von `TableFormatter` zu erstellen, ohne die Funktion `print_table()` zu ändern. Auf diese Weise können wir in Zukunft verschiedene Ausgabeformate wie CSV oder HTML unterstützen.
