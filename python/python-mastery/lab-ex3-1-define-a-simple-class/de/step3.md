# Formatieren und Ausgeben der Portfolio - Daten

In diesem Schritt werden wir eine Funktion erstellen, die uns hilft, Portfolio - Daten in einer gut organisierten Tabelle anzuzeigen. Ein Portfolio ist eine Sammlung von Aktien, und es ist wichtig, diese Daten auf klare und lesbare Weise darzustellen. Hier kommt die Funktion `print_portfolio(portfolio)` ins Spiel. Diese Funktion nimmt ein Portfolio als Eingabe und zeigt es in einer Tabelle mit Überschriften und korrekter Ausrichtung an.

## String - Formatierung in Python

In Python gibt es mehrere Möglichkeiten, Strings zu formatieren. Die String - Formatierung ist eine entscheidende Fähigkeit, da sie es Ihnen ermöglicht, Daten auf organisierte und benutzerfreundliche Weise darzustellen.

- Der `%` - Operator ist ein älteres Formatierungsverfahren für Strings. Es ist wie eine Vorlage, in der Sie Werte an bestimmten Stellen in einem String einfügen können.
- Die Methode `str.format()` ist eine andere Möglichkeit. Sie bietet mehr Flexibilität und eine sauberere Syntax für die String - Formatierung.
- f - Strings sind eine Funktion, die ab Python 3.6 eingeführt wurde. Sie sind sehr praktisch, da sie es Ihnen ermöglichen, Ausdrücke direkt in String - Literalen einzubetten.

Für diese Übung verwenden wir den `%` - Operator. Er ist besonders nützlich, wenn Sie Spalten mit fester Breite erstellen möchten, was genau für unsere Portfolio - Tabelle erforderlich ist.

## Implementierungsanweisungen

1. Öffnen Sie zunächst die Datei `stock.py` in Ihrem Editor. Wenn sie bereits geöffnet ist, ist das gut. In dieser Datei werden wir unsere `print_portfolio` - Funktion schreiben.

2. Sobald die Datei geöffnet ist, suchen Sie nach dem Kommentar `# TODO: Add print_portfolio(portfolio) function here`. Dieser Kommentar ist ein Marker, der uns sagt, wo wir unsere neue Funktion hinzufügen sollen.

3. Unterhalb dieses Kommentars fügen Sie die folgende Funktion hinzu:

```python
def print_portfolio(portfolio):
    """
    Print the portfolio data in a nicely formatted table.

    Args:
        portfolio (list): A list of Stock objects
    """
    # Print the header row
    print('%10s %10s %10s' % ('name', 'shares', 'price'))

    # Print a separator line
    print('-' * 10 + ' ' + '-' * 10 + ' ' + '-' * 10)

    # Print each stock in the portfolio
    for stock in portfolio:
        print('%10s %10d %10.2f' % (stock.name, stock.shares, stock.price))
```

Diese Funktion gibt zunächst die Kopfzeile der Tabelle aus, dann eine Trennlinie und schließlich durchläuft sie jedes Aktienobjekt im Portfolio und gibt seine Details in formatierter Form aus.

4. Nach dem Hinzufügen der Funktion speichern Sie die Datei. Sie können dies tun, indem Sie `Strg+S` drücken oder "Datei > Speichern" aus dem Menü auswählen. Das Speichern der Datei stellt sicher, dass Ihre Änderungen beibehalten werden.

5. Jetzt müssen wir unsere Funktion testen. Erstellen Sie eine neue Datei namens `test_print.py`. Diese Datei wird unser Testskript sein. Fügen Sie den folgenden Code hinzu:

```python
# test_print.py
from stock import read_portfolio, print_portfolio

# Read the portfolio from the CSV file
portfolio = read_portfolio('portfolio.csv')

# Print the portfolio as a formatted table
print_portfolio(portfolio)
```

Dieses Skript importiert die Funktionen `read_portfolio` und `print_portfolio` aus der Datei `stock.py`. Dann liest es die Portfolio - Daten aus einer CSV - Datei und verwendet unsere neu erstellte `print_portfolio` - Funktion, um sie anzuzeigen.

6. Abschließend führen Sie das Testskript aus. Öffnen Sie Ihr Terminal und geben Sie den folgenden Befehl ein:

```bash
python3 test_print.py
```

Wenn alles korrekt funktioniert, sollten Sie eine Ausgabe wie die folgende sehen:

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

Diese Ausgabe bestätigt, dass Ihre `print_portfolio` - Funktion wie erwartet funktioniert. Sie formatiert und zeigt die Portfolio - Daten in einer Tabelle mit Überschriften und ausgerichteten Spalten an, was es einfach macht, die Daten zu lesen.

## Verständnis der String - Formatierung

Schauen wir uns genauer an, wie die String - Formatierung in der `print_portfolio` - Funktion funktioniert.

- `%10s` wird verwendet, um einen String zu formatieren. Die `10` gibt die Breite des Feldes an, und das `s` steht für String. Es richtet den String rechtsbündig in einem Feld der Breite 10 aus.
- `%10d` ist für die Formatierung einer Ganzzahl. Die `10` ist die Feldbreite, und `d` steht für Ganzzahl. Es richtet die Ganzzahl ebenfalls rechtsbündig in einem Feld der Breite 10 aus.
- `%10.2f` wird für die Formatierung einer Gleitkommazahl verwendet. Die `10` ist die Feldbreite, und das `.2` gibt an, dass wir die Gleitkommazahl mit 2 Dezimalstellen anzeigen möchten. Es richtet die Gleitkommazahl rechtsbündig in einem Feld der Breite 10 aus.

Diese Formatierung stellt sicher, dass alle Spalten in unserer Tabelle richtig ausgerichtet sind, was die Ausgabe viel einfacher zu lesen und zu verstehen macht.
