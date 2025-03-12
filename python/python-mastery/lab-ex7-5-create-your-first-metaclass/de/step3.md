# Die Verwendung Ihrer Metaklasse

Jetzt werden wir eine Klasse erstellen, die unsere Metaklasse über Vererbung nutzt. Dies wird uns helfen zu verstehen, wie die Metaklasse aufgerufen wird, wenn die Klasse definiert wird.

Eine Metaklasse in Python ist eine Klasse, die andere Klassen erstellt. Wenn Sie eine Klasse definieren, verwendet Python eine Metaklasse, um das Klassenobjekt zu konstruieren. Durch die Verwendung von Vererbung können wir angeben, welche Metaklasse eine Klasse verwenden soll.

1. Öffnen Sie `mymeta.py` und fügen Sie am Ende der Datei folgenden Code hinzu:

```python
class Stock(myobject):
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def cost(self):
        return self.shares * self.price

    def sell(self, nshares):
        self.shares -= nshares
```

Hier definieren wir eine `Stock`-Klasse, die von `myobject` erbt. Die `__init__`-Methode ist eine spezielle Methode in Python-Klassen. Sie wird aufgerufen, wenn ein Objekt der Klasse erstellt wird und dient zur Initialisierung der Attribute des Objekts. Die `cost`-Methode berechnet die Gesamtkosten der Aktie, und die `sell`-Methode verringert die Anzahl der Aktien.

2. Speichern Sie die Datei, indem Sie Strg+S drücken. Das Speichern der Datei stellt sicher, dass die von Ihnen vorgenommenen Änderungen gespeichert werden und später ausgeführt werden können.

3. Jetzt lassen Sie uns die Datei ausführen, um zu sehen, was passiert. Öffnen Sie ein Terminal im WebIDE und führen Sie aus:

```bash
cd /home/labex/project
python3 mymeta.py
```

Der `cd`-Befehl wechselt das aktuelle Arbeitsverzeichnis zu `/home/labex/project`, und `python3 mymeta.py` führt das Python-Skript `mymeta.py` aus.

Sie sollten eine Ausgabe ähnlich der folgenden sehen:

```
Creating class : myobject
Base classes   : ()
Attributes     : ['__module__', '__qualname__', '__doc__']
Creating class : Stock
Base classes   : (<class '__main__.myobject'>,)
Attributes     : ['__module__', '__qualname__', '__init__', 'cost', 'sell', '__doc__']
```

Diese Ausgabe zeigt, dass unsere Metaklasse aufgerufen wird, wenn sowohl die `myobject`- als auch die `Stock`-Klasse erstellt werden. Beachten Sie, wie:

- Für `Stock` die Basisklassen `myobject` enthalten, da `Stock` von `myobject` erbt.
- Die Attributliste alle von uns definierten Methoden (`__init__`, `cost`, `sell`) sowie einige Standardattribute enthält.

4. Lassen Sie uns mit unserer `Stock`-Klasse interagieren. Erstellen Sie eine neue Datei namens `test_stock.py` mit folgendem Inhalt:

```python
# test_stock.py
from mymeta import Stock

# Create a new Stock instance
apple = Stock("AAPL", 100, 154.50)

# Use the methods
print(f"Stock: {apple.name}, Shares: {apple.shares}, Price: ${apple.price}")
print(f"Total cost: ${apple.cost()}")

# Sell some shares
apple.sell(10)
print(f"After selling 10 shares: {apple.shares} shares remaining")
print(f"Updated cost: ${apple.cost()}")
```

In diesem Code importieren wir die `Stock`-Klasse aus dem `mymeta`-Modul. Dann erstellen wir eine Instanz der `Stock`-Klasse namens `apple`. Wir verwenden die Methoden der `Stock`-Klasse, um Informationen über die Aktie auszugeben, die Gesamtkosten zu berechnen, einige Aktien zu verkaufen und dann die aktualisierten Informationen auszugeben.

5. Führen Sie diese Datei aus, um unsere `Stock`-Klasse zu testen:

```bash
python3 test_stock.py
```

Sie sollten eine Ausgabe wie die folgende sehen:

```
Creating class : myobject
Base classes   : ()
Attributes     : ['__module__', '__qualname__', '__doc__']
Creating class : Stock
Base classes   : (<class 'mymeta.myobject'>,)
Attributes     : ['__module__', '__qualname__', '__init__', 'cost', 'sell', '__doc__']
Stock: AAPL, Shares: 100, Price: $154.5
Total cost: $15450.0
After selling 10 shares: 90 shares remaining
Updated cost: $13905.0
```

Beachten Sie, dass zuerst die Informationen unserer Metaklasse ausgegeben werden, gefolgt von der Ausgabe unseres Testskripts. Dies liegt daran, dass die Metaklasse aufgerufen wird, wenn die Klasse definiert wird, was vor der Ausführung des Codes im Testskript geschieht.
