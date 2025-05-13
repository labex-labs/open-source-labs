# Das Problem mit der Spaltenformatierung verstehen

In diesem Schritt werden wir uns eine Einschränkung in unserer aktuellen Implementierung der Tabellenformatierung ansehen. Wir werden auch einige mögliche Lösungen für dieses Problem untersuchen.

Zuerst wollen wir verstehen, was wir tun werden. Wir öffnen den VSCode-Editor und betrachten die Datei `tableformat.py` im Projektverzeichnis. Diese Datei ist wichtig, weil sie den Code enthält, der es uns ermöglicht, tabellarische Daten auf verschiedene Arten zu formatieren, z. B. in Text-, CSV- oder HTML-Formaten.

Um die Datei zu öffnen, verwenden wir die folgenden Befehle im Terminal. Der Befehl `cd` wechselt das Verzeichnis in das Projektverzeichnis, und der Befehl `code` öffnet die Datei `tableformat.py` in VSCode.

```bash
cd ~/project
touch tableformat.py
```

Wenn Sie die Datei öffnen, werden Sie feststellen, dass mehrere Klassen definiert sind. Diese Klassen spielen unterschiedliche Rollen bei der Formatierung der Tabellendaten.

- `TableFormatter`: Dies ist eine abstrakte Basisklasse (abstract base class). Sie hat Methoden, die für die Formatierung der Tabellenüberschriften und -zeilen verwendet werden. Stellen Sie sie sich als eine Blaupause für andere Formatiererklassen vor.
- `TextTableFormatter`: Diese Klasse wird verwendet, um die Tabelle im Klartextformat auszugeben.
- `CSVTableFormatter`: Sie ist verantwortlich für die Formatierung der Tabellendaten im CSV-Format (Comma-Separated Values).
- `HTMLTableFormatter`: Diese Klasse formatiert die Tabellendaten im HTML-Format.

Es gibt auch eine Funktion `print_table()` in der Datei. Diese Funktion verwendet die Formatiererklassen, die wir gerade erwähnt haben, um die tabellarischen Daten anzuzeigen.

Sehen wir uns nun an, wie diese Klassen funktionieren. Erstellen Sie in Ihrem Verzeichnis `/home/labex/project` eine neue Datei namens `step1_test1.py` mit Ihrem Editor oder dem Befehl `touch`. Fügen Sie den folgenden Python-Code hinzu:

```python
# step1_test1.py
from tableformat import print_table, TextTableFormatter, portfolio

formatter = TextTableFormatter()
print("--- Running Step 1 Test 1 ---")
print_table(portfolio, ['name', 'shares', 'price'], formatter)
print("-----------------------------")
```

Speichern Sie die Datei und führen Sie sie von Ihrem Terminal aus:

```bash
python3 step1_test1.py
```

Nachdem Sie das Skript ausgeführt haben, sollten Sie eine ähnliche Ausgabe wie diese sehen:

```
--- Running Step 1 Test 1 ---
      name     shares      price
---------- ---------- ----------
        AA        100       32.2
       IBM         50       91.1
       CAT        150      83.44
      MSFT        200      51.23
        GE         95      40.37
      MSFT         50       65.1
       IBM        100      70.44
-----------------------------
```

Lassen Sie uns nun das Problem finden. Beachten Sie, dass die Werte in der Spalte `price` nicht einheitlich formatiert sind. Einige Werte haben eine Dezimalstelle, wie 32.2, während andere zwei Dezimalstellen haben, wie 51.23. Bei Finanzdaten möchten wir in der Regel, dass die Formatierung einheitlich ist.

So soll die Ausgabe aussehen:

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

Eine Möglichkeit, dies zu beheben, besteht darin, die Funktion `print_table()` so zu ändern, dass sie Formatangaben akzeptiert. Lassen Sie uns sehen, wie das funktioniert, _ohne_ `tableformat.py` tatsächlich zu ändern. Erstellen Sie eine neue Datei namens `step1_test2.py` mit dem folgenden Inhalt. Dieses Skript definiert die Funktion `print_table` lokal zu Demonstrationszwecken neu.

```python
# step1_test2.py
from tableformat import TextTableFormatter

# Re-define Stock and portfolio locally for this example
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

portfolio = [
    Stock('AA', 100, 32.20), Stock('IBM', 50, 91.10), Stock('CAT', 150, 83.44),
    Stock('MSFT', 200, 51.23), Stock('GE', 95, 40.37), Stock('MSFT', 50, 65.10),
    Stock('IBM', 100, 70.44)
]

# Define a modified print_table locally
def print_table_modified(records, fields, formats, formatter):
    formatter.headings(fields)
    for r in records:
        # Apply formats to the original attribute values
        rowdata = [(fmt % getattr(r, fieldname))
                   for fieldname, fmt in zip(fields, formats)]
        # Pass the already formatted strings to the formatter's row method
        formatter.row(rowdata)

print("--- Running Step 1 Test 2 ---")
formatter = TextTableFormatter()
# Note: TextTableFormatter.row expects strings already formatted for width.
# This example might not align perfectly yet, but demonstrates passing formats.
print_table_modified(portfolio,
                     ['name', 'shares', 'price'],
                     ['%10s', '%10d', '%10.2f'], # Using widths
                     formatter)
print("-----------------------------")

```

Führen Sie dieses Skript aus:

```bash
python3 step1_test2.py
```

Dieser Ansatz demonstriert das Übergeben von Formaten, aber das Ändern von `print_table` hat einen Nachteil: Das Ändern der Schnittstelle (interface) der Funktion könnte bestehenden Code beschädigen, der die Originalversion verwendet.

Ein anderer Ansatz ist die Erstellung eines benutzerdefinierten Formatierers (custom formatter) durch Subclassing (Unterklassenbildung). Wir können eine neue Klasse erstellen, die von `TextTableFormatter` erbt und die Methode `row()` überschreibt (override). Erstellen Sie eine Datei `step1_test3.py`:

```python
# step1_test3.py
from tableformat import TextTableFormatter, print_table, portfolio

class PortfolioFormatter(TextTableFormatter):
    def row(self, rowdata):
        # Example: Add a prefix to demonstrate overriding
        # Note: The original lab description's formatting example had data type issues
        # because print_table sends strings to this method. This is a simpler demo.
        print("> ", end="") # Add a simple prefix to the line start
        super().row(rowdata) # Call the parent method

print("--- Running Step 1 Test 3 ---")
formatter = PortfolioFormatter()
print_table(portfolio, ['name', 'shares', 'price'], formatter)
print("-----------------------------")
```

Führen Sie das Skript aus:

```bash
python3 step1_test3.py
```

Diese Lösung funktioniert, um Subclassing zu demonstrieren, aber das Erstellen einer neuen Klasse für jede Formatierungsvariation ist nicht praktikabel. Außerdem sind Sie an die Basisklasse (base class) gebunden, von der Sie erben (hier `TextTableFormatter`).

Im nächsten Schritt werden wir eine elegantere Lösung mit Mixin-Klassen untersuchen.
