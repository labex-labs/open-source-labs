# Das Erstellen eines Tabellenformatierers mithilfe des Attributzugriffs

In der Programmierung ist der Attributzugriff ein grundlegendes Konzept, das es uns ermöglicht, mit den Eigenschaften von Objekten zu interagieren. Jetzt werden wir das, was wir über den Attributzugriff gelernt haben, in die Praxis umsetzen. Wir werden ein nützliches Werkzeug erstellen: einen Tabellenformatierer. Dieser Formatierer nimmt eine Sammlung von Objekten und zeigt sie in tabellarischer Form an, wodurch die Daten leichter lesbar und verständlich werden.

## Das Erstellen des `tableformat.py`-Moduls

Zunächst müssen wir eine neue Python-Datei erstellen. Diese Datei wird den Code für unseren Tabellenformatierer enthalten.

Um die Datei zu erstellen, folgen Sie diesen Schritten:

1. Klicken Sie im WebIDE auf das Menü "File".
2. Wählen Sie aus der Dropdown-Liste "New File" aus.
3. Speichern Sie die neu erstellte Datei als `tableformat.py` im Verzeichnis `/home/labex/project/`.

Jetzt, da wir unsere Datei haben, schreiben wir den Code für die `print_table()`-Funktion in `tableformat.py`. Diese Funktion wird für die Formatierung und Ausgabe unserer Objekte in einer Tabelle verantwortlich sein.

```python
def print_table(objects, fields):
    """
    Print a collection of objects as a formatted table.

    Args:
        objects: A sequence of objects
        fields: A list of attribute names
    """
    # Print the header
    headers = fields
    for header in headers:
        print(f"{header:>10}", end=' ')
    print()

    # Print the separator line
    for header in headers:
        print("-" * 10, end=' ')
    print()

    # Print the data
    for obj in objects:
        for field in fields:
            value = getattr(obj, field)
            print(f"{value:>10}", end=' ')
        print()
```

Lassen Sie uns analysieren, was diese Funktion tut:

1. Sie nimmt zwei Argumente entgegen: eine Sequenz von Objekten und eine Liste von Attributnamen. Die Sequenz von Objekten ist die Daten, die wir anzeigen möchten, und die Liste von Attributnamen sagt der Funktion, welche Eigenschaften der Objekte angezeigt werden sollen.
2. Sie gibt eine Kopfzeile aus. Die Kopfzeile enthält die Namen der Attribute, an denen wir interessiert sind.
3. Sie gibt eine Trennlinie aus. Diese Linie hilft, den Kopf von den Daten visuell zu trennen.
4. Für jedes Objekt in der Sequenz gibt sie den Wert jedes angegebenen Attributs aus. Sie verwendet die `getattr()`-Funktion, um auf den Attributwert jedes Objekts zuzugreifen.

Jetzt testen wir unsere `print_table()`-Funktion, um zu sehen, ob sie wie erwartet funktioniert.

```python
# Open a Python interactive shell
python3

# Import our modules
from stock import read_portfolio
import tableformat

# Read the portfolio data
portfolio = read_portfolio('portfolio.csv')

# Print the portfolio as a table with name, shares, and price columns
tableformat.print_table(portfolio, ['name', 'shares', 'price'])
```

Wenn Sie den obigen Code ausführen, sollten Sie die folgende Ausgabe sehen:

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

Einer der großen Vorteile unserer `print_table()`-Funktion ist ihre Flexibilität. Wir können die angezeigten Spalten einfach ändern, indem wir die `fields`-Liste ändern.

```python
# Just show shares and name
tableformat.print_table(portfolio, ['shares', 'name'])
```

Das Ausführen dieses Codes gibt Ihnen die folgende Ausgabe:

```
    shares       name
---------- ----------
       100         AA
        50        IBM
       150        CAT
       200       MSFT
        95         GE
        50       MSFT
       100        IBM
```

Die Stärke dieses Ansatzes liegt in seiner Allgemeingültigkeit. Wir können die gleiche `print_table()`-Funktion verwenden, um Tabellen für jeden Objekttyp auszugeben, solange wir die Namen der Attribute kennen, die wir anzeigen möchten. Dies macht unseren Tabellenformatierer zu einem sehr nützlichen Werkzeug in unserem Programmierwerkzeugkasten.
