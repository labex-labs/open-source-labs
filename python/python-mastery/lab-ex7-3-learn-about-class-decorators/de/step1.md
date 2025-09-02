# Implementierung der Typüberprüfung mit Deskriptoren

In diesem Schritt erstellen wir eine `Stock`-Klasse, die Deskriptoren zur Typüberprüfung verwendet. Aber zuerst wollen wir verstehen, was Deskriptoren sind. Deskriptoren sind ein wirklich mächtiges Feature in Python. Sie geben Ihnen die Kontrolle darüber, wie auf Attribute in Klassen zugegriffen wird.

Deskriptoren sind Objekte, die definieren, wie auf Attribute anderer Objekte zugegriffen wird. Dies geschieht durch die Implementierung spezieller Methoden wie `__get__`, `__set__` und `__delete__`. Diese Methoden ermöglichen es Deskriptoren, den Abruf, die Zuweisung und das Löschen von Attributen zu verwalten. Deskriptoren sind sehr nützlich für die Implementierung von Validierung, Typüberprüfung und berechneten Eigenschaften. Sie können beispielsweise einen Deskriptor verwenden, um sicherzustellen, dass ein Attribut immer eine positive Zahl oder ein String eines bestimmten Formats ist.

Die Datei `validate.py` enthält bereits Validator-Klassen (`String`, `PositiveInteger`, `PositiveFloat`). Wir können diese Klassen verwenden, um die Attribute unserer `Stock`-Klasse zu validieren.

Nun erstellen wir unsere `Stock`-Klasse mit Deskriptoren.

1. Öffnen Sie zuerst die Datei `stock.py` in Ihrem Editor.

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

Lassen Sie uns aufschlüsseln, was dieser Code tut. Das `_fields`-Tupel definiert die Attribute der `Stock`-Klasse. Dies sind die Namen der Attribute, die unsere `Stock`-Objekte haben werden.

Die Attribute `name`, `shares` und `price` sind als Deskriptorobjekte definiert. Der `String()`-Deskriptor stellt sicher, dass das `name`-Attribut ein String ist. Der `PositiveInteger()`-Deskriptor stellt sicher, dass das `shares`-Attribut eine positive Ganzzahl ist. Und der `PositiveFloat()`-Deskriptor garantiert, dass das `price`-Attribut eine positive Gleitkommazahl ist.

Die `cost`-Eigenschaft ist eine berechnete Eigenschaft. Sie berechnet die Gesamtkosten des Stocks basierend auf der Anzahl der Aktien und dem Preis pro Aktie.

Die `sell`-Methode wird verwendet, um die Anzahl der Aktien zu reduzieren. Wenn Sie diese Methode mit einer zu verkaufenden Aktienanzahl aufrufen, zieht sie diese Anzahl vom `shares`-Attribut ab.

Die Zeile `Stock.create_init()` erstellt dynamisch eine `__init__`-Methode für unsere Klasse. Diese Methode ermöglicht es uns, `Stock`-Objekte zu erstellen, indem wir die Werte für die Attribute `name`, `shares` und `price` übergeben.

3. Nachdem Sie den Code hinzugefügt haben, speichern Sie die Datei. Dadurch wird sichergestellt, dass Ihre Änderungen gespeichert werden und bei der Ausführung der Tests verwendet werden können.

4. Führen wir nun die Tests aus, um Ihre Implementierung zu überprüfen. Wechseln Sie zuerst mit dem folgenden Befehl in das Verzeichnis `~/project`:

```bash
cd ~/project
```

Führen Sie dann die Tests mit dem folgenden Befehl aus:

```bash
python3 teststock.py
```

Wenn Ihre Implementierung korrekt ist, sollten Sie eine Ausgabe ähnlich dieser sehen:

```
.........
----------------------------------------------------------------------
Ran 9 tests in 0.001s

OK
```

Diese Ausgabe bedeutet, dass alle Tests bestanden wurden. Die Deskriptoren validieren erfolgreich die Typen jedes Attributs!

Versuchen wir, ein `Stock`-Objekt im Python-Interpreter zu erstellen. Stellen Sie zunächst sicher, dass Sie sich im Verzeichnis `~/project` befinden. Führen Sie dann den folgenden Befehl aus:

```bash
cd ~/project
python3 -c "from stock import Stock; s = Stock('GOOG', 100, 490.1); print(s); print(f'Cost: {s.cost}')"
```

Sie sollten die folgende Ausgabe sehen:

```
Stock('GOOG', 100, 490.1)
Cost: 49010.0
```

Sie haben erfolgreich Deskriptoren für die Typüberprüfung implementiert! Lassen Sie uns diesen Code nun weiter verbessern.
