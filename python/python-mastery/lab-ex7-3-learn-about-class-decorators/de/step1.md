# Implementierung von Typüberprüfung mit Deskriptoren

In diesem Schritt werden wir eine `Stock`-Klasse erstellen, die Deskriptoren (descriptors) zur Typüberprüfung verwendet. Aber zunächst verstehen wir, was Deskriptoren sind. Deskriptoren sind eine sehr leistungsstarke Funktion in Python. Sie ermöglichen es Ihnen, die Art und Weise zu kontrollieren, wie Attribute in Klassen zugegriffen werden.

Deskriptoren sind Objekte, die definieren, wie auf Attribute anderer Objekte zugegriffen wird. Sie tun dies, indem sie spezielle Methoden wie `__get__`, `__set__` und `__delete__` implementieren. Diese Methoden ermöglichen es den Deskriptoren, zu verwalten, wie Attribute abgerufen, festgelegt und gelöscht werden. Deskriptoren sind sehr nützlich für die Implementierung von Validierung, Typüberprüfung und berechneten Eigenschaften. Beispielsweise können Sie einen Deskriptor verwenden, um sicherzustellen, dass ein Attribut immer eine positive Zahl oder eine Zeichenkette eines bestimmten Formats ist.

Die Datei `validate.py` enthält bereits Validator-Klassen (`String`, `PositiveInteger`, `PositiveFloat`). Wir können diese Klassen verwenden, um die Attribute unserer `Stock`-Klasse zu validieren.

Jetzt erstellen wir unsere `Stock`-Klasse mit Deskriptoren.

1. Öffnen Sie zunächst die Datei `stock.py` im Editor. Sie können dies tun, indem Sie den folgenden Befehl in Ihrem Terminal ausführen:

```bash
code ~/project/stock.py
```

Dieser Befehl verwendet den `code`-Editor, um die Datei `stock.py` im Verzeichnis `~/project` zu öffnen.

2. Sobald die Datei geöffnet ist, ersetzen Sie den Platzhalterinhalt durch den folgenden Code:

```python
# stock.py

from structure import Structure
from validate import String, PositiveInteger, PositiveFloat

class Stock(Structure):
    _fields = ('name', 'shares', 'price')
    name = String()
    shares = PositiveInteger()
    price = PositiveFloat()

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, nshares):
        self.shares -= nshares

# Create an __init__ method based on _fields
Stock.create_init()
```

Lassen Sie uns analysieren, was dieser Code tut. Das Tupel `_fields` definiert die Attribute der `Stock`-Klasse. Dies sind die Namen der Attribute, die unsere `Stock`-Objekte haben werden.

Die Attribute `name`, `shares` und `price` sind als Deskriptor-Objekte definiert. Der `String()`-Deskriptor stellt sicher, dass das `name`-Attribut eine Zeichenkette ist. Der `PositiveInteger()`-Deskriptor sorgt dafür, dass das `shares`-Attribut eine positive Ganzzahl ist. Und der `PositiveFloat()`-Deskriptor garantiert, dass das `price`-Attribut eine positive Fließkommazahl ist.

Die `cost`-Eigenschaft ist eine berechnete Eigenschaft. Sie berechnet die Gesamtkosten der Aktie basierend auf der Anzahl der Aktien und dem Preis pro Aktie.

Die `sell`-Methode wird verwendet, um die Anzahl der Aktien zu reduzieren. Wenn Sie diese Methode mit einer Anzahl von Aktien zum Verkauf aufrufen, subtrahiert sie diese Anzahl vom `shares`-Attribut.

Die Zeile `Stock.create_init()` erstellt dynamisch eine `__init__`-Methode für unsere Klasse. Diese Methode ermöglicht es uns, `Stock`-Objekte zu erstellen, indem wir die Werte für die Attribute `name`, `shares` und `price` übergeben.

3. Nachdem Sie den Code hinzugefügt haben, speichern Sie die Datei. Dadurch werden Ihre Änderungen gespeichert und können verwendet werden, wenn Sie die Tests ausführen.

4. Jetzt führen wir die Tests aus, um Ihre Implementierung zu überprüfen. Ändern Sie zunächst das Verzeichnis in das `~/project`-Verzeichnis, indem Sie den folgenden Befehl ausführen:

```bash
cd ~/project
```

Führen Sie dann die Tests mit dem folgenden Befehl aus:

```bash
python3 teststock.py
```

Wenn Ihre Implementierung korrekt ist, sollten Sie eine Ausgabe ähnlich der folgenden sehen:

```
.........
----------------------------------------------------------------------
Ran 9 tests in 0.001s

OK
```

Diese Ausgabe bedeutet, dass alle Tests bestanden werden. Die Deskriptoren validieren erfolgreich die Typen jedes Attributs!

Versuchen wir, ein `Stock`-Objekt in der Python-Shell zu erstellen. Stellen Sie zunächst sicher, dass Sie sich im Verzeichnis `~/project` befinden. Führen Sie dann den folgenden Befehl aus:

```bash
cd ~/project
python3 -c "from stock import Stock; s = Stock('GOOG', 100, 490.1); print(s); print(f'Cost: {s.cost}')"
```

Sie sollten die folgende Ausgabe sehen:

```
Stock('GOOG', 100, 490.1)
Cost: 49010.0
```

Sie haben erfolgreich Deskriptoren für die Typüberprüfung implementiert! Jetzt verbessern wir diesen Code weiter.
