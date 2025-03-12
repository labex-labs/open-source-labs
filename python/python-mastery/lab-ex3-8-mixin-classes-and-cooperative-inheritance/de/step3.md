# Erstellen einer benutzerfreundlichen API für Mixins

Mixins sind eine leistungsstarke Funktion in Python, aber sie können für Anfänger etwas schwierig sein, da sie Mehrfachvererbung (multiple inheritance) betreffen, die recht komplex werden kann. In diesem Schritt werden wir es den Benutzern einfacher machen, indem wir die Funktion `create_formatter()` verbessern. Auf diese Weise müssen sich die Benutzer nicht so sehr um die Details der Mehrfachvererbung kümmern.

Zunächst müssen Sie die Datei `tableformat.py` öffnen. Sie können dies tun, indem Sie die folgenden Befehle in Ihrem Terminal ausführen. Der Befehl `cd` wechselt das Verzeichnis in Ihren Projektordner, und der Befehl `code` öffnet die Datei `tableformat.py` in Ihrem Code-Editor.

```bash
cd ~/project
code tableformat.py
```

Sobald die Datei geöffnet ist, suchen Sie die Funktion `create_formatter()`. Derzeit sieht sie so aus:

```python
def create_formatter(name):
    """
    Create an appropriate formatter based on the name.
    """
    if name == 'text':
        return TextTableFormatter()
    elif name == 'csv':
        return CSVTableFormatter()
    elif name == 'html':
        return HTMLTableFormatter()
    else:
        raise RuntimeError(f'Unknown format {name}')
```

Diese Funktion nimmt einen Namen als Argument und gibt den entsprechenden Formatter zurück. Aber wir möchten sie flexibler machen. Wir werden sie so ändern, dass sie optionale Argumente für unsere Mixins akzeptieren kann.

Ersetzen Sie die vorhandene Funktion `create_formatter()` durch die verbesserte Version unten. Diese neue Funktion ermöglicht es Ihnen, Spaltenformate und festzulegen, ob die Überschriften in Großbuchstaben umgewandelt werden sollen.

```python
def create_formatter(name, column_formats=None, upper_headers=False):
    """
    Create a formatter with optional enhancements.

    Parameters:
    name : str
        Name of the formatter ('text', 'csv', 'html')
    column_formats : list, optional
        List of format strings for column formatting
    upper_headers : bool, optional
        Whether to convert headers to uppercase
    """
    if name == 'text':
        formatter_cls = TextTableFormatter
    elif name == 'csv':
        formatter_cls = CSVTableFormatter
    elif name == 'html':
        formatter_cls = HTMLTableFormatter
    else:
        raise RuntimeError(f'Unknown format {name}')

    # Apply mixins if requested
    if column_formats and upper_headers:
        class CustomFormatter(ColumnFormatMixin, UpperHeadersMixin, formatter_cls):
            formats = column_formats
        return CustomFormatter()
    elif column_formats:
        class CustomFormatter(ColumnFormatMixin, formatter_cls):
            formats = column_formats
        return CustomFormatter()
    elif upper_headers:
        class CustomFormatter(UpperHeadersMixin, formatter_cls):
            pass
        return CustomFormatter()
    else:
        return formatter_cls()
```

Diese verbesserte Funktion funktioniert, indem sie zunächst die Basis-Formatter-Klasse anhand des Arguments `name` bestimmt. Dann, je nachdem, ob `column_formats` und `upper_headers` angegeben werden, erstellt sie eine benutzerdefinierte Formatter-Klasse, die die entsprechenden Mixins enthält. Schließlich gibt sie eine Instanz der benutzerdefinierten Formatter-Klasse zurück.

Jetzt testen wir unsere verbesserte Funktion mit verschiedenen Kombinationen von Optionen.

Zunächst versuchen wir die Spaltenformatierung. Führen Sie den folgenden Befehl in Ihrem Terminal aus. Dieser Befehl importiert die erforderlichen Funktionen und Daten aus der Datei `tableformat.py`, erstellt einen Formatter mit Spaltenformatierung und gibt dann eine Tabelle mit diesem Formatter aus.

```python
python3 -c "
from tableformat import create_formatter, portfolio, print_table

formatter = create_formatter('text', column_formats=['%s', '%d', '%0.2f'])
print_table(portfolio, ['name', 'shares', 'price'], formatter)
"
```

Sie sollten die Tabelle mit formatierten Spalten sehen. Die Ausgabe wird so aussehen:

```
      name     shares      price
---------- ---------- ----------
        AA        100      32.20
       IBM         50      91.10
       CAT        150      83.44
      MSFT        200      51.23
        GE         95      40.37
      MSFT         50      65.10
       IBM        100      70.44
```

Als Nächstes versuchen wir die Verwendung von Großbuchstabenüberschriften. Führen Sie den folgenden Befehl aus:

```python
python3 -c "
from tableformat import create_formatter, portfolio, print_table

formatter = create_formatter('text', upper_headers=True)
print_table(portfolio, ['name', 'shares', 'price'], formatter)
"
```

Sie sollten die Tabelle mit Großbuchstabenüberschriften sehen. Die Ausgabe wird sein:

```
      NAME     SHARES      PRICE
---------- ---------- ----------
        AA        100       32.2
       IBM         50       91.1
       CAT        150      83.44
      MSFT        200      51.23
        GE         95      40.37
      MSFT         50       65.1
       IBM        100      70.44
```

Schließlich kombinieren wir beide Optionen. Führen Sie diesen Befehl aus:

```python
python3 -c "
from tableformat import create_formatter, portfolio, print_table

formatter = create_formatter('text', column_formats=['%s', '%d', '%0.2f'], upper_headers=True)
print_table(portfolio, ['name', 'shares', 'price'], formatter)
"
```

Dies sollte eine Tabelle mit formatierten Spalten und Großbuchstabenüberschriften anzeigen. Die Ausgabe wird sein:

```
      NAME     SHARES      PRICE
---------- ---------- ----------
        AA        100      32.20
       IBM         50      91.10
       CAT        150      83.44
      MSFT        200      51.23
        GE         95      40.37
      MSFT         50      65.10
       IBM        100      70.44
```

Die verbesserte Funktion funktioniert auch mit anderen Formatter-Typen. Beispielsweise versuchen wir es mit dem CSV-Formatter. Führen Sie den folgenden Befehl aus:

```python
python3 -c "
from tableformat import create_formatter, portfolio, print_table

formatter = create_formatter('csv', column_formats=['\\"%s\\"', '%d', '%0.2f'])
print_table(portfolio, ['name', 'shares', 'price'], formatter)
"
```

Dies sollte eine CSV-Ausgabe mit formatierten Spalten erzeugen. Die Ausgabe wird sein:

```
name,shares,price
"AA",100,32.20
"IBM",50,91.10
"CAT",150,83.44
"MSFT",200,51.23
"GE",95,40.37
"MSFT",50,65.10
"IBM",100,70.44
```

Durch die Verbesserung der Funktion `create_formatter()` haben wir eine benutzerfreundliche API erstellt. Benutzer können jetzt einfach Mixins verwenden, ohne die komplexen Details der Mehrfachvererbung verstehen zu müssen. Dies gibt ihnen die Flexibilität, die Formatter nach ihren Bedürfnissen anzupassen.
