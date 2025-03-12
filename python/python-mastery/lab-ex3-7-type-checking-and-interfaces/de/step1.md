# Hinzufügen von Typüberprüfung zu print_table()

In diesem Schritt werden wir die Funktion `print_table()` in der Datei `tableformat.py` verbessern. Wir werden eine Überprüfung hinzufügen, um zu sehen, ob der Parameter `formatter` eine gültige Instanz von `TableFormatter` ist. Warum brauchen wir das? Nun, Typüberprüfung ist wie ein Sicherheitsnetz für Ihren Code. Sie hilft sicherzustellen, dass die Daten, mit denen Sie arbeiten, vom richtigen Typ sind, was viele schwer zu findende Fehler vermeiden kann.

## Verständnis der Typüberprüfung in Python

Typüberprüfung ist eine sehr nützliche Technik in der Programmierung. Sie ermöglicht es Ihnen, Fehler früh im Entwicklungsprozess zu erkennen. In Python arbeiten wir oft mit verschiedenen Objekttypen, und manchmal erwarten wir, dass ein bestimmter Objekttyp an eine Funktion übergeben wird. Um zu überprüfen, ob ein Objekt von einem bestimmten Typ oder einer Unterklasse davon ist, können wir die Funktion `isinstance()` verwenden. Beispielsweise, wenn Sie eine Funktion haben, die eine Liste erwartet, können Sie `isinstance()` verwenden, um sicherzustellen, dass die Eingabe tatsächlich eine Liste ist.

## Modifizieren der print_table()-Funktion

Öffnen Sie zunächst die Datei `tableformat.py` in Ihrem Code-Editor. Scrollen Sie nach unten bis zum Ende der Datei, und Sie finden die Funktion `print_table()`. So sieht sie zunächst aus:

```python
def print_table(data, columns, formatter):
    '''
    Print a table showing selected columns from a data source
    using the given formatter.
    '''
    formatter.headings(columns)
    for item in data:
        rowdata = [str(getattr(item, col)) for col in columns]
        formatter.row(rowdata)
```

Diese Funktion nimmt einige Daten, eine Liste von Spalten und einen Formatter entgegen. Anschließend verwendet sie den Formatter, um eine Tabelle auszugeben. Aber im Moment wird nicht überprüft, ob der Formatter vom richtigen Typ ist.

Lassen Sie uns es modifizieren, um die Typüberprüfung hinzuzufügen. Wir verwenden die Funktion `isinstance()`, um zu überprüfen, ob der Parameter `formatter` eine Instanz von `TableFormatter` ist. Wenn dies nicht der Fall ist, werfen wir einen `TypeError` mit einer klaren Nachricht. Hier ist der modifizierte Code:

```python
def print_table(data, columns, formatter):
    '''
    Print a table showing selected columns from a data source
    using the given formatter.
    '''
    if not isinstance(formatter, TableFormatter):
        raise TypeError("Expected a TableFormatter")

    formatter.headings(columns)
    for item in data:
        rowdata = [str(getattr(item, col)) for col in columns]
        formatter.row(rowdata)
```

## Testen Ihrer Typüberprüfungsimplementierung

Jetzt, da wir die Typüberprüfung hinzugefügt haben, müssen wir sicherstellen, dass sie funktioniert. Lassen Sie uns eine neue Python-Datei namens `test_tableformat.py` erstellen. Hier ist der Code, den Sie hineinschreiben sollten:

```python
import stock
import reader
import tableformat

# Read portfolio data
portfolio = reader.read_csv_as_instances('portfolio.csv', stock.Stock)

# Define a formatter that doesn't inherit from TableFormatter
class MyFormatter:
    def headings(self, headers):
        pass
    def row(self, rowdata):
        pass

# Try to use the non-compliant formatter
try:
    tableformat.print_table(portfolio, ['name', 'shares', 'price'], MyFormatter())
    print("Test failed - type checking not implemented")
except TypeError as e:
    print(f"Test passed - caught error: {e}")
```

In diesem Code lesen wir zunächst einige Portfolio-Daten. Dann definieren wir eine neue Formatter-Klasse namens `MyFormatter`, die nicht von `TableFormatter` erbt. Wir versuchen, diesen nicht konformen Formatter in der Funktion `print_table()` zu verwenden. Wenn unsere Typüberprüfung funktioniert, sollte ein `TypeError` ausgelöst werden.

Um den Test auszuführen, öffnen Sie Ihr Terminal und navigieren Sie zum Verzeichnis, in dem sich die Datei `test_tableformat.py` befindet. Führen Sie dann den folgenden Befehl aus:

```bash
python test_tableformat.py
```

Wenn alles korrekt funktioniert, sollten Sie eine Ausgabe wie diese sehen:

```
Test passed - caught error: Expected a TableFormatter
```

Diese Ausgabe bestätigt, dass unsere Typüberprüfung wie erwartet funktioniert. Jetzt wird die Funktion `print_table()` nur einen Formatter akzeptieren, der eine Instanz von `TableFormatter` oder einer seiner Unterklassen ist.
