# Das Problem mit der Spaltenformatierung verstehen

In diesem Schritt werden wir uns eine Einschränkung in unserer aktuellen Tabellenformatierungs-Implementierung anschauen. Wir werden auch einige mögliche Lösungen für dieses Problem untersuchen.

Zunächst verstehen wir, was wir tun werden. Wir öffnen den VSCode-Editor und betrachten die Datei `tableformat.py` im Projektverzeichnis. Diese Datei ist wichtig, da sie den Code enthält, der es uns ermöglicht, tabellarische Daten auf verschiedene Weise zu formatieren, wie z. B. im Text-, CSV- oder HTML-Format.

Um die Datei zu öffnen, verwenden wir die folgenden Befehle im Terminal. Der Befehl `cd` wechselt das Verzeichnis in das Projektverzeichnis, und der Befehl `code` öffnet die Datei `tableformat.py` in VSCode.

```bash
cd ~/project
code tableformat.py
```

Wenn Sie die Datei öffnen, werden Sie feststellen, dass mehrere Klassen definiert sind. Diese Klassen spielen unterschiedliche Rollen bei der Formatierung der Tabellendaten.

- `TableFormatter`: Dies ist eine abstrakte Basisklasse. Sie hat Methoden, die zur Formatierung der Tabellenüberschriften und -zeilen verwendet werden. Stellen Sie sich dies als ein Bauplan für andere Formatiererklassen vor.
- `TextTableFormatter`: Diese Klasse wird verwendet, um die Tabelle im Klartextformat auszugeben.
- `CSVTableFormatter`: Sie ist für die Formatierung der Tabellendaten im CSV-Format (Comma-Separated Values, engl. für "durch Kommas getrennte Werte") verantwortlich.
- `HTMLTableFormatter`: Diese Klasse formatiert die Tabellendaten im HTML-Format.

Es gibt auch eine Funktion `print_table()` in der Datei. Diese Funktion verwendet die gerade erwähnten Formatiererklassen, um die tabellarischen Daten anzuzeigen.

Jetzt sehen wir uns an, wie diese Klassen funktionieren, indem wir etwas Python-Code ausführen. Öffnen Sie ein Terminal und starten Sie eine Python-Sitzung. Der folgende Code importiert die erforderlichen Funktionen und Klassen aus der Datei `tableformat.py`, erstellt ein `TextTableFormatter`-Objekt und verwendet dann die Funktion `print_table()`, um die Portfolio-Daten anzuzeigen.

```python
python3 -c "
from tableformat import print_table, TextTableFormatter, portfolio
formatter = TextTableFormatter()
print_table(portfolio, ['name', 'shares', 'price'], formatter)
"
```

Nachdem Sie den Code ausgeführt haben, sollten Sie eine Ausgabe ähnlich der folgenden sehen:

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

Jetzt suchen wir das Problem. Beachten Sie, dass die Werte in der Spalte `price` nicht konsistent formatiert sind. Einige Werte haben eine Dezimalstelle, wie 32.2, während andere zwei Dezimalstellen haben, wie 51.23. Bei Finanzdaten möchten wir normalerweise, dass die Formatierung konsistent ist.

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

Eine Möglichkeit, dies zu beheben, besteht darin, die Funktion `print_table()` zu ändern, um Formatangaben zu akzeptieren. Der folgende Code zeigt, wie wir dies tun können. Wir definieren eine neue Funktion `print_table()`, die einen zusätzlichen Parameter `formats` nimmt. Innerhalb der Funktion verwenden wir diese Formatangaben, um jeden Wert in der Zeile zu formatieren.

```python
python3 -c "
from tableformat import TextTableFormatter, portfolio

def print_table(records, fields, formats, formatter):
    formatter.headings(fields)
    for r in records:
        rowdata = [(fmt % getattr(r, fieldname))
             for fieldname, fmt in zip(fields, formats)]
        formatter.row(rowdata)

formatter = TextTableFormatter()
print_table(portfolio,
            ['name','shares','price'],
            ['%s','%d','%0.2f'],
            formatter)
"
```

Diese Lösung funktioniert, hat aber einen Nachteil. Das Ändern der Schnittstelle der Funktion kann bestehenden Code, der die alte Version der Funktion `print_table()` verwendet, beschädigen.

Ein anderer Ansatz besteht darin, einen benutzerdefinierten Formatierer durch Subklassen zu erstellen. Wir können eine neue Klasse erstellen, die von `TextTableFormatter` erbt, und die Methode `row()` überschreiben, um die gewünschte Formatierung anzuwenden.

```python
python3 -c "
from tableformat import TextTableFormatter, print_table, portfolio

class PortfolioFormatter(TextTableFormatter):
    def row(self, rowdata):
        formats = ['%s','%d','%0.2f']
        rowdata = [(fmt % d) for fmt, d in zip(formats, rowdata)]
        super().row(rowdata)

formatter = PortfolioFormatter()
print_table(portfolio, ['name','shares','price'], formatter)
"
```

Diese Lösung funktioniert ebenfalls, ist aber nicht sehr praktisch. Jedes Mal, wenn wir eine andere Formatierung möchten, müssen wir eine neue Klasse erstellen. Und wir sind auf den spezifischen Formatierertyp beschränkt, von dem wir ableiten, in diesem Fall `TextTableFormatter`.

Im nächsten Schritt werden wir eine elegantere Lösung mit Mixin-Klassen (Mixin-Klassen sind in der Informatik eine spezielle Art von Klasse) untersuchen.
