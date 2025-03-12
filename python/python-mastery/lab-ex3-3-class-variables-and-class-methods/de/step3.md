# Klassenvariablen und Vererbung

In diesem Schritt werden wir untersuchen, wie Klassenvariablen mit Vererbung interagieren und wie sie als Mechanismus zur Anpassung dienen können. In Python ermöglicht die Vererbung einer Unterklasse, Attribute und Methoden von einer Basisklasse zu erben. Klassenvariablen sind Variablen, die zur Klasse selbst gehören, nicht zu einer bestimmten Instanz der Klasse. Das Verständnis, wie diese zusammenwirken, ist entscheidend für die Erstellung von flexiblen und wartbaren Code.

## Klassenvariablen bei der Vererbung

Wenn eine Unterklasse von einer Basisklasse erbt, hat sie automatisch Zugang zu den Klassenvariablen der Basisklasse. Die Unterklasse kann jedoch diese Klassenvariablen überschreiben. Dadurch kann die Unterklasse ihr Verhalten ändern, ohne die Basisklasse zu beeinflussen. Dies ist eine sehr mächtige Funktion, da sie es Ihnen ermöglicht, das Verhalten einer Unterklasse gemäß Ihren spezifischen Anforderungen anzupassen.

## Erstellung einer spezialisierten Stock-Klasse

Erstellen wir eine Unterklasse der `Stock`-Klasse. Wir nennen sie `DStock`, was für Decimal Stock steht. Der Hauptunterschied zwischen `DStock` und der normalen `Stock`-Klasse besteht darin, dass `DStock` den `Decimal`-Typ für Preiswerte anstelle von `float` verwendet. Bei Finanzberechnungen ist Präzision äußerst wichtig, und der `Decimal`-Typ bietet genauere Dezimalarithmetik im Vergleich zu `float`.

Um diese Unterklasse zu erstellen, erstellen wir eine neue Datei namens `decimal_stock.py`. Hier ist der Code, den Sie in diese Datei einfügen müssen:

```python
# decimal_stock.py
from decimal import Decimal
from stock import Stock

class DStock(Stock):
    """
    A specialized version of Stock that uses Decimal for prices
    """
    types = (str, int, Decimal)  # Override the types class variable

# Test the subclass
if __name__ == "__main__":
    # Create a DStock from row data
    row = ['AA', '100', '32.20']
    ds = DStock.from_row(row)

    print(f"DStock: {ds.name}")
    print(f"Shares: {ds.shares}")
    print(f"Price: {ds.price} (type: {type(ds.price).__name__})")
    print(f"Cost: {ds.cost()} (type: {type(ds.cost()).__name__})")

    # For comparison, create a regular Stock from the same data
    s = Stock.from_row(row)
    print(f"\nRegular Stock: {s.name}")
    print(f"Shares: {s.shares}")
    print(f"Price: {s.price} (type: {type(s.price).__name__})")
    print(f"Cost: {s.cost()} (type: {type(s.cost()).__name__})")
```

Nachdem Sie die Datei `decimal_stock.py` mit dem obigen Code erstellt haben, müssen Sie sie ausführen, um die Ergebnisse zu sehen. Öffnen Sie Ihr Terminal und befolgen Sie diese Schritte:

```bash
cd ~/project
python decimal_stock.py
```

Sie sollten eine Ausgabe ähnlich der folgenden sehen:

```
DStock: AA
Shares: 100
Price: 32.20 (type: Decimal)
Cost: 3220.0 (type: Decimal)

Regular Stock: AA
Shares: 100
Price: 32.2 (type: float)
Cost: 3220.0 (type: float)
```

## Wichtige Punkte zu Klassenvariablen und Vererbung

Aus diesem Beispiel können wir mehrere wichtige Schlussfolgerungen ziehen:

1. Die `DStock`-Klasse erbt alle Methoden von der `Stock`-Klasse, wie z. B. die `cost()`-Methode, ohne sie neu definieren zu müssen. Dies ist einer der Hauptvorteile der Vererbung, da es Ihnen erspart, redundantem Code zu schreiben.
2. Durch das einfache Überschreiben der `types`-Klassenvariablen haben wir geändert, wie Daten bei der Erstellung neuer `DStock`-Instanzen konvertiert werden. Dies zeigt, wie Klassenvariablen verwendet werden können, um das Verhalten einer Unterklasse anzupassen.
3. Die Basisklasse `Stock` bleibt unverändert und funktioniert weiterhin mit `float`-Werten. Dies bedeutet, dass die Änderungen, die wir an der Unterklasse vorgenommen haben, die Basisklasse nicht beeinflussen, was ein gutes Designprinzip ist.
4. Die `from_row()`-Klassenmethode funktioniert korrekt sowohl mit der `Stock`- als auch mit der `DStock`-Klasse. Dies zeigt die Stärke der Vererbung, da dieselbe Methode mit verschiedenen Unterklassen verwendet werden kann.

Dieses Beispiel zeigt deutlich, wie Klassenvariablen als Konfigurationsmechanismus verwendet werden können. Unterklassen können diese Variablen überschreiben, um ihr Verhalten anzupassen, ohne die Methoden neu schreiben zu müssen.

## Design-Diskussion

Betrachten wir einen alternativen Ansatz, bei dem wir die Typkonvertierungen in die `__init__`-Methode legen:

```python
class Stock:
    def __init__(self, name, shares, price):
        self.name = str(name)
        self.shares = int(shares)
        self.price = float(price)
```

Mit diesem Ansatz können wir ein `Stock`-Objekt aus einer Zeile von Daten wie folgt erstellen:

```python
row = ['AA', '100', '32.20']
s = Stock(*row)
```

Obwohl dieser Ansatz auf den ersten Blick einfacher erscheinen mag, hat er mehrere Nachteile:

1. Er vereint zwei verschiedene Anliegen: die Objekterstellung und die Datenkonvertierung. Dies macht den Code schwieriger zu verstehen und zu warten.
2. Die `__init__`-Methode wird weniger flexibel, da sie die Eingaben immer konvertiert, auch wenn sie bereits im richtigen Typ sind.
3. Er beschränkt die Möglichkeit der Unterklassen, den Konvertierungsprozess anzupassen. Unterklassen hätten Schwierigkeiten, die Konvertierungslogik zu ändern, wenn sie in der `__init__`-Methode eingebettet ist.
4. Der Code wird anfälliger. Wenn eine der Konvertierungen fehlschlägt, kann das Objekt nicht erstellt werden, was zu Fehlern in Ihrem Programm führen kann.

Andererseits trennt der Ansatz mit Klassenmethoden diese Anliegen. Dies macht den Code wartbarer und flexibler, da jeder Teil des Codes nur eine einzige Verantwortung hat.
