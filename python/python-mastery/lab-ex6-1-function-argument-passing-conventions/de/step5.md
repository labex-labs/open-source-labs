# Umgestaltung der Stock-Klasse

Nachdem wir nun eine gut definierte Basisklasse `Structure` haben, ist es an der Zeit, unsere `Stock`-Klasse neu zu schreiben. Durch die Verwendung dieser Basisklasse können wir unseren Code vereinfachen und besser organisieren. Die `Structure`-Klasse bietet eine Reihe von gemeinsamen Funktionen, die wir in unserer `Stock`-Klasse wiederverwenden können, was ein großer Vorteil für die Wartbarkeit und Lesbarkeit des Codes ist.

## Erstellung der neuen Stock-Klasse

Beginnen wir damit, eine neue Datei namens `stock.py` zu erstellen. Diese Datei wird unsere umgeschriebene `Stock`-Klasse enthalten. Hier ist der Code, den Sie in die `stock.py`-Datei einfügen müssen:

```python
# stock.py
from structure import Structure

class Stock(Structure):
    _fields = ('name', 'shares', 'price')

    @property
    def cost(self):
        """
        Calculate the cost as shares * price
        """
        return self.shares * self.price

    def sell(self, nshares):
        """
        Sell a number of shares
        """
        self.shares -= nshares
```

Lassen Sie uns analysieren, was diese neue `Stock`-Klasse tut:

1. Sie erbt von der `Structure`-Klasse. Dies bedeutet, dass die `Stock`-Klasse alle von der `Structure`-Klasse bereitgestellten Funktionen nutzen kann. Einer der Vorteile ist, dass wir keine eigene `__init__`-Methode schreiben müssen, da die `Structure`-Klasse die Attributzuweisung automatisch übernimmt.
2. Wir definieren `_fields`, ein Tupel, das die Attribute der `Stock`-Klasse angibt. Diese Attribute sind `name`, `shares` und `price`.
3. Die Eigenschaft `cost` wird definiert, um die Gesamtkosten der Aktie zu berechnen. Sie multipliziert die Anzahl der `shares` mit dem `price`.
4. Die Methode `sell` wird verwendet, um die Anzahl der Aktien zu reduzieren. Wenn Sie diese Methode mit einer Anzahl von Aktien zum Verkauf aufrufen, wird diese Anzahl von der aktuellen Anzahl der Aktien subtrahiert.

## Testen der neuen Stock-Klasse

Um sicherzustellen, dass unsere neue `Stock`-Klasse wie erwartet funktioniert, müssen wir eine Testdatei erstellen. Erstellen Sie eine Datei namens `test_stock.py` mit dem folgenden Code:

```python
# test_stock.py
from stock import Stock

# Create a stock
s = Stock('GOOG', 100, 490.1)

# Check the attributes
print(f"Stock: {s}")
print(f"Name: {s.name}")
print(f"Shares: {s.shares}")
print(f"Price: {s.price}")
print(f"Cost: {s.cost}")

# Sell some shares
print("\nSelling 20 shares...")
s.sell(20)
print(f"Shares after selling: {s.shares}")
print(f"Cost after selling: {s.cost}")

# Try to set an invalid attribute
print("\nTrying to set an invalid attribute:")
try:
    s.prices = 500  # Invalid attribute (should be 'price')
    print("This should not print")
except AttributeError as e:
    print(f"Error correctly caught: {e}")
```

In dieser Testdatei importieren wir zunächst die `Stock`-Klasse aus der `stock.py`-Datei. Dann erstellen wir eine Instanz der `Stock`-Klasse mit dem Namen 'GOOG', 100 Aktien und einem Preis von 490,1. Wir geben die Attribute der Aktie aus, um zu überprüfen, ob sie korrekt festgelegt sind. Danach verkaufen wir 20 Aktien und geben die neue Anzahl der Aktien und die neuen Kosten aus. Schließlich versuchen wir, ein ungültiges Attribut `prices` festzulegen (es sollte `price` sein). Wenn unsere `Stock`-Klasse korrekt funktioniert, sollte sie einen `AttributeError` auslösen.

Um den Test auszuführen, öffnen Sie Ihr Terminal und geben Sie den folgenden Befehl ein:

```bash
python3 test_stock.py
```

Die erwartete Ausgabe ist wie folgt:

```
Stock: Stock('GOOG', 100, 490.1)
Name: GOOG
Shares: 100
Price: 490.1
Cost: 49010.0

Selling 20 shares...
Shares after selling: 80
Cost after selling: 39208.0

Trying to set an invalid attribute:
Error correctly caught: No attribute prices
```

## Ausführen von Unittests

Wenn Sie aus vorherigen Übungen Unittests haben, können Sie sie gegen Ihre neue Implementierung ausführen. Geben Sie in Ihrem Terminal den folgenden Befehl ein:

```bash
python3 teststock.py
```

Beachten Sie, dass einige Tests fehlschlagen können. Dies kann daran liegen, dass sie bestimmte Verhaltensweisen oder Methoden erwarten, die wir noch nicht implementiert haben. Machen Sie sich keine Sorgen! Wir werden in zukünftigen Übungen auf dieser Grundlage aufbauen.

## Rückblick auf unseren Fortschritt

Nehmen wir einen Moment Zeit, um zu überprüfen, was wir bisher erreicht haben:

1. Wir haben eine wiederverwendbare Basisklasse `Structure` erstellt. Diese Klasse:

   - Übernimmt automatisch die Attributzuweisung, wodurch wir viel wiederholenden Code sparen.
   - Bietet eine gute Zeichenkettenrepräsentation, was es erleichtert, unsere Objekte auszugeben und zu debuggen.
   - Beschränkt die Attributnamen, um Fehler zu vermeiden, was unseren Code robuster macht.

2. Wir haben unsere `Stock`-Klasse neu geschrieben. Sie:
   - Erbt von der `Structure`-Klasse, um die gemeinsamen Funktionen wiederzuverwenden.
   - Definiert nur die Felder und domänenspezifischen Methoden, was die Klasse fokussiert und sauber hält.
   - Hat ein klares und einfaches Design, das es leicht zu verstehen und zu warten macht.

Dieser Ansatz hat mehrere Vorteile für unseren Code:

- Er ist besser wartbar, da wir weniger Wiederholungen haben. Wenn wir etwas in der gemeinsamen Funktionalität ändern müssen, müssen wir es nur in der `Structure`-Klasse ändern.
- Er ist robuster, aufgrund der besseren Fehlersuche, die von der `Structure`-Klasse bereitgestellt wird.
- Er ist leichter lesbar, da die Verantwortlichkeiten jeder Klasse klar sind.

In zukünftigen Übungen werden wir auf dieser Grundlage aufbauen, um ein ausgefeilteres System zur Verwaltung von Aktienportfolios zu erstellen.
