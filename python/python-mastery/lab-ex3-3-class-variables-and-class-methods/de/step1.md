# Verständnis von Klassenvariablen und Klassenmethoden

In diesem ersten Schritt werden wir uns mit den Konzepten von Klassenvariablen und Klassenmethoden in Python vertraut machen. Dies sind wichtige Konzepte, die Ihnen helfen, effizienteren und besser organisierten Code zu schreiben. Bevor wir mit Klassenvariablen und Klassenmethoden beginnen, schauen wir uns zunächst an, wie Instanzen unserer `Stock`-Klasse derzeit erstellt werden. Dies gibt uns ein Grundverständnis und zeigt uns, wo wir Verbesserungen vornehmen können.

## Was sind Klassenvariablen?

Klassenvariablen sind eine besondere Art von Variablen in Python. Sie werden von allen Instanzen einer Klasse geteilt. Um dies besser zu verstehen, vergleichen wir sie mit Instanzvariablen. Instanzvariablen sind für jede Instanz einer Klasse einzigartig. Wenn Sie beispielsweise mehrere Instanzen einer Klasse haben, kann jede Instanz ihren eigenen Wert für eine Instanzvariable haben. Klassenvariablen hingegen werden auf Klassenebene definiert. Das bedeutet, dass alle Instanzen dieser Klasse auf denselben Wert der Klassenvariablen zugreifen und ihn teilen können.

## Was sind Klassenmethoden?

Klassenmethoden sind Methoden, die auf der Klasse selbst arbeiten, nicht auf einzelnen Instanzen der Klasse. Sie sind an die Klasse gebunden, was bedeutet, dass sie direkt auf der Klasse aufgerufen werden können, ohne eine Instanz zu erstellen. Um eine Klassenmethode in Python zu definieren, verwenden wir den `@classmethod`-Decorator. Anstelle der Instanz (`self`) als ersten Parameter nehmen Klassenmethoden die Klasse (`cls`) als ersten Parameter. Dies ermöglicht es ihnen, auf Klassenebendaten zu operieren und Aktionen im Zusammenhang mit der Klasse als Ganzes auszuführen.

## Aktueller Ansatz zur Erstellung von Stock-Instanzen

Schauen wir uns zunächst an, wie wir derzeit Instanzen der `Stock`-Klasse erstellen. Öffnen Sie die Datei `stock.py` im Editor, um die aktuelle Implementierung zu betrachten:

```python
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def cost(self):
        return self.shares * self.price
```

Instanzen dieser Klasse werden normalerweise auf eine der folgenden Arten erstellt:

1. Direkte Initialisierung mit Werten:

   ```python
   s = Stock('GOOG', 100, 490.1)
   ```

   Hier erstellen wir direkt eine Instanz der `Stock`-Klasse, indem wir die Werte für die Attribute `name`, `shares` und `price` angeben. Dies ist eine einfache Möglichkeit, eine Instanz zu erstellen, wenn Sie die Werte im Voraus kennen.

2. Erstellung aus Daten, die aus einer CSV-Datei gelesen wurden:
   ```python
   import csv
   with open('portfolio.csv') as f:
       rows = csv.reader(f)
       headers = next(rows)  # Skip the header
       row = next(rows)      # Get the first data row
       s = Stock(row[0], int(row[1]), float(row[2]))
   ```
   Wenn wir Daten aus einer CSV-Datei lesen, liegen die Werte zunächst im String-Format vor. Wenn wir also eine `Stock`-Instanz aus CSV-Daten erstellen, müssen wir die String-Werte manuell in die entsprechenden Typen umwandeln. Beispielsweise muss der `shares`-Wert in einen Integer und der `price`-Wert in einen Float umgewandelt werden.

Probieren wir dies aus. Erstellen Sie eine neue Python-Datei namens `test_stock.py` im Verzeichnis `~/project` mit folgendem Inhalt:

```python
# test_stock.py
from stock import Stock
import csv

# Method 1: Direct creation
s1 = Stock('GOOG', 100, 490.1)
print(f"Stock: {s1.name}, Shares: {s1.shares}, Price: {s1.price}")
print(f"Cost: {s1.cost()}")

# Method 2: Creation from CSV row
with open('portfolio.csv') as f:
    rows = csv.reader(f)
    headers = next(rows)  # Skip the header
    row = next(rows)      # Get the first data row
    s2 = Stock(row[0], int(row[1]), float(row[2]))
    print(f"\nStock from CSV: {s2.name}, Shares: {s2.shares}, Price: {s2.price}")
    print(f"Cost: {s2.cost()}")
```

Führen Sie diese Datei aus, um die Ergebnisse zu sehen:

```bash
cd ~/project
python test_stock.py
```

Sie sollten eine Ausgabe ähnlich der folgenden sehen:

```
Stock: GOOG, Shares: 100, Price: 490.1
Cost: 49010.0

Stock from CSV: AA, Shares: 100, Price: 32.2
Cost: 3220.0
```

Diese manuelle Umwandlung funktioniert, hat aber einige Nachteile. Wir müssen das genaue Format der Daten kennen, und wir müssen die Umwandlungen jedes Mal durchführen, wenn wir eine Instanz aus CSV-Daten erstellen. Dies kann fehleranfällig und zeitaufwendig sein. Im nächsten Schritt werden wir eine elegantere Lösung mithilfe von Klassenmethoden erstellen.
