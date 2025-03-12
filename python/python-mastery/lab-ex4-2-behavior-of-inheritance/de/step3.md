# Anwenden von Validatoren auf eine Aktienklasse

In diesem Schritt werden wir sehen, wie unsere Validatoren in einer realen Situation funktionieren. Validatoren sind wie kleine Prüfer, die sicherstellen, dass die Daten, die wir verwenden, bestimmten Regeln entsprechen. Wir werden eine `Stock`-Klasse erstellen. Eine Klasse ist wie ein Bauplan für die Erstellung von Objekten. In diesem Fall wird die `Stock`-Klasse eine Aktie an der Börse repräsentieren, und wir werden unsere Validatoren verwenden, um sicherzustellen, dass die Werte ihrer Attribute (wie die Anzahl der Anteile und der Preis) gültig sind.

## Erstellen der Aktienklasse

Zunächst müssen wir eine neue Datei erstellen. In der WebIDE erstellen Sie eine neue Datei namens `stock.py`. Diese Datei wird den Code für unsere `Stock`-Klasse enthalten. Fügen Sie nun den folgenden Code in die `stock.py`-Datei ein:

```python
# stock.py
from validate import PositiveInteger, PositiveFloat

class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    @property
    def shares(self):
        return self._shares

    @shares.setter
    def shares(self, value):
        self._shares = PositiveInteger.check(value)

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = PositiveFloat.check(value)

    def cost(self):
        return self.shares * self.price
```

Lassen Sie uns analysieren, was dieser Code tut:

1. Wir beginnen damit, die `PositiveInteger`- und `PositiveFloat`-Validatoren aus unserem `validate`-Modul zu importieren. Diese Validatoren helfen uns, sicherzustellen, dass die Anzahl der Anteile eine positive Ganzzahl und der Preis eine positive Fließkommazahl ist.
2. Dann definieren wir eine `Stock`-Klasse. Innerhalb der Klasse haben wir eine `__init__`-Methode. Diese Methode wird aufgerufen, wenn wir ein neues `Stock`-Objekt erstellen. Sie nimmt drei Parameter entgegen: `name`, `shares` und `price` und weist sie den Attributen des Objekts zu.
3. Wir verwenden Properties und Setter, um die Werte von `shares` und `price` zu validieren. Ein Property ist eine Möglichkeit, den Zugriff auf ein Attribut zu steuern, und ein Setter ist eine Methode, die aufgerufen wird, wenn wir versuchen, den Wert dieses Attributs zu setzen. Wenn wir das `shares`-Attribut setzen, wird die `PositiveInteger.check`-Methode aufgerufen, um sicherzustellen, dass der Wert eine positive Ganzzahl ist. Ebenso wird, wenn wir das `price`-Attribut setzen, die `PositiveFloat.check`-Methode aufgerufen, um sicherzustellen, dass der Wert eine positive Fließkommazahl ist.
4. Schließlich haben wir eine `cost`-Methode. Diese Methode berechnet die Gesamtkosten der Aktie, indem sie die Anzahl der Anteile mit dem Preis multipliziert.

## Testen der Aktienklasse

Jetzt, da wir unsere `Stock`-Klasse erstellt haben, müssen wir sie testen, um zu sehen, ob die Validatoren korrekt funktionieren. Öffnen Sie ein neues Terminal und starten Sie den Python-Interpreter. Sie können dies tun, indem Sie den folgenden Befehl ausführen:

```bash
python3
```

Sobald der Python-Interpreter läuft, können wir unsere `Stock`-Klasse importieren und testen. Geben Sie den folgenden Code in den Python-Interpreter ein:

```python
from stock import Stock

# Create a valid stock
s = Stock('GOOG', 100, 490.10)
print(f"Name: {s.name}, Shares: {s.shares}, Price: {s.price}")
print(f"Cost: {s.cost()}")

# Try setting an invalid shares value
try:
    s.shares = -10
except ValueError as e:
    print(f"Error setting shares: {e}")

# Try setting an invalid price value
try:
    s.price = "not a price"
except TypeError as e:
    print(f"Error setting price: {e}")
```

Wenn Sie diesen Code ausführen, sollten Sie eine Ausgabe ähnlich der folgenden sehen:

```
Name: GOOG, Shares: 100, Price: 490.1
Cost: 49010.0
Error setting shares: Expected >= 0
Error setting price: Expected <class 'float'>
```

Diese Ausgabe zeigt, dass unsere Validatoren wie erwartet funktionieren. Die `Stock`-Klasse lässt uns keine ungültigen Werte für `shares` und `price` setzen. Wenn wir versuchen, einen ungültigen Wert zu setzen, wird ein Fehler ausgelöst, und wir können diesen Fehler abfangen und ausgeben.

## Verständnis, wie Vererbung hilft

Einer der großen Vorteile der Verwendung unserer Validatoren ist, dass wir verschiedene Validierungsregeln leicht kombinieren können. Vererbung ist ein mächtiges Konzept in Python, das es uns ermöglicht, neue Klassen auf der Grundlage bestehender zu erstellen. Mit multipler Vererbung können wir die `super()`-Funktion verwenden, um Methoden aus mehreren Elternklassen aufzurufen.

Beispielsweise, wenn wir sicherstellen möchten, dass der Name der Aktie nicht leer ist, können wir die folgenden Schritte ausführen:

1. Importieren Sie den `NonEmptyString`-Validator aus dem `validate`-Modul. Dieser Validator hilft uns, zu überprüfen, ob der Name der Aktie kein leerer String ist.
2. Fügen Sie einen Property-Setter für das `name`-Attribut in der `Stock`-Klasse hinzu. Dieser Setter wird die `NonEmptyString.check()`-Methode verwenden, um den Namen der Aktie zu validieren.

Dies zeigt, wie Vererbung, insbesondere multiple Vererbung mit der `super()`-Funktion, es uns ermöglicht, Komponenten zu erstellen, die flexibel sind und in verschiedenen Kombinationen wiederverwendet werden können.

Wenn Sie mit dem Testen fertig sind, können Sie den Python-Interpreter beenden, indem Sie den folgenden Befehl ausführen:

```python
exit()
```
