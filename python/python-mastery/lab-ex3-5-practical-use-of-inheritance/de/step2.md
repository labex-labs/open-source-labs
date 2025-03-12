# Erstellen einer Basisklasse und Ändern der Ausgabefunktion

In der Programmierung ist Vererbung (inheritance) ein mächtiges Konzept, das es uns ermöglicht, eine Hierarchie von Klassen zu erstellen. Um Vererbung für die Ausgabe von Daten in verschiedenen Formaten zu nutzen, müssen wir zunächst eine Basisklasse erstellen. Eine Basisklasse dient als Blaupause für andere Klassen und definiert eine gemeinsame Gruppe von Methoden, die ihre Unterklassen erben und überschreiben können.

Jetzt erstellen wir eine Basisklasse, die die Schnittstelle für alle Tabellenformatierer definiert. Öffnen Sie die Datei `tableformat.py` im WebIDE und fügen Sie den folgenden Code oben in der Datei hinzu:

```python
class TableFormatter:
    """
    Base class for all table formatters.
    This class defines the interface that all formatters must implement.
    """
    def headings(self, headers):
        """
        Generate the table headings.
        """
        raise NotImplementedError()

    def row(self, rowdata):
        """
        Generate a single row of table data.
        """
        raise NotImplementedError()
```

Die Klasse `TableFormatter` ist eine abstrakte Basisklasse. Eine abstrakte Basisklasse ist eine Klasse, die Methoden definiert, aber keine Implementierungen für sie bereitstellt. Stattdessen erwartet sie, dass ihre Unterklassen diese Implementierungen liefern. Die `NotImplementedError` - Ausnahmen werden verwendet, um anzuzeigen, dass diese Methoden von Unterklassen überschrieben werden müssen. Wenn eine Unterklasse diese Methoden nicht überschreibt und wir versuchen, sie zu verwenden, wird ein Fehler ausgelöst.

Als Nächstes müssen wir die Funktion `print_table()` ändern, um die Klasse `TableFormatter` zu verwenden. Die Funktion `print_table()` wird verwendet, um eine Tabelle mit Daten aus einer Liste von Objekten auszugeben. Indem wir sie so ändern, dass sie die Klasse `TableFormatter` verwendet, können wir die Funktion flexibler gestalten und sie in der Lage machen, mit verschiedenen Tabellenformaten zu arbeiten.

Ersetzen Sie die vorhandene Funktion `print_table()` durch den folgenden Code:

```python
def print_table(records, fields, formatter):
    """
    Print a table of data from a list of objects using the specified formatter.

    Args:
        records: A list of objects
        fields: A list of field names
        formatter: A TableFormatter object
    """
    formatter.headings(fields)
    for r in records:
        rowdata = [getattr(r, fieldname) for fieldname in fields]
        formatter.row(rowdata)
```

Der wichtigste Unterschied hier ist, dass `print_table()` jetzt einen `formatter` - Parameter nimmt, der eine Instanz von `TableFormatter` oder einer Unterklasse sein sollte. Dies bedeutet, dass wir verschiedene Tabellenformatierer an die Funktion `print_table()` übergeben können, und sie wird den entsprechenden Formatierer verwenden, um die Tabelle auszugeben. Die Funktion delegiert die Formatierungsaufgabe an das Formatierer - Objekt, indem sie seine Methoden `headings()` und `row()` aufruft.

Testen wir unsere Änderungen, indem wir versuchen, die Basisklasse `TableFormatter` zu verwenden:

```python
import stock
import reader
import tableformat

portfolio = reader.read_csv_as_instances('portfolio.csv', stock.Stock)
formatter = tableformat.TableFormatter()
tableformat.print_table(portfolio, ['name', 'shares', 'price'], formatter)
```

Wenn Sie diesen Code ausführen, sollten Sie einen Fehler sehen:

```
Traceback (most recent call last):
...
NotImplementedError
```

Dieser Fehler tritt auf, weil wir versuchen, die abstrakte Basisklasse direkt zu verwenden, aber sie keine Implementierungen für ihre Methoden bereitstellt. Da die Methoden `headings()` und `row()` in der Klasse `TableFormatter` `NotImplementedError` auslösen, weiß Python nicht, was es tun soll, wenn diese Methoden aufgerufen werden. Im nächsten Schritt werden wir eine konkrete Unterklasse erstellen, die diese Implementierungen bereitstellt.
