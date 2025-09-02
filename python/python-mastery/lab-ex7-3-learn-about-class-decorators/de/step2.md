# Erstellung eines Klassendekorators für die Validierung

Im vorherigen Schritt funktionierte unsere Implementierung, aber es gab eine Redundanz. Wir mussten sowohl das `_fields`-Tupel als auch die Deskriptorattribute angeben. Das ist nicht sehr effizient und wir können es verbessern. In Python sind Klassendekoratoren ein mächtiges Werkzeug, das uns helfen kann, diesen Prozess zu vereinfachen. Ein Klassendekorator ist eine Funktion, die eine Klasse als Argument nimmt, sie auf eine bestimmte Weise modifiziert und dann die modifizierte Klasse zurückgibt. Durch die Verwendung eines Klassendekorators können wir Feldinformationen automatisch aus den Deskriptoren extrahieren, was unseren Code sauberer und wartbarer macht.

Erstellen wir einen Klassendekorator, um unseren Code zu vereinfachen. Hier sind die Schritte, die Sie befolgen müssen:

1. Öffnen Sie zuerst die Datei `structure.py` in Ihrem Editor.

2. Fügen Sie als Nächstes den folgenden Code am Anfang der Datei `structure.py` hinzu, direkt nach allen Importanweisungen. Dieser Code definiert unseren Klassendekorator:

```python
from validate import Validator

def validate_attributes(cls):
    """
    Class decorator that extracts Validator instances
    and builds the _fields list automatically
    """
    validators = []
    for name, val in vars(cls).items():
        if isinstance(val, Validator):
            validators.append(val)

    # Set _fields based on validator names
    cls._fields = [val.name for val in validators]

    # Create initialization method
    cls.create_init()

    return cls
```

Lassen Sie uns aufschlüsseln, was dieser Dekorator tut:

- Er erstellt zuerst eine leere Liste namens `validators`. Dann durchläuft er alle Attribute der Klasse mit `vars(cls).items()`. Wenn ein Attribut eine Instanz der `Validator`-Klasse ist, fügt er dieses Attribut der Liste `validators` hinzu.
- Danach setzt er das Attribut `_fields` der Klasse. Er erstellt eine Liste von Namen aus den Validatoren in der Liste `validators` und weist sie `cls._fields` zu.
- Schließlich ruft er die Methode `create_init()` der Klasse auf, um die `__init__`-Methode zu generieren, und gibt dann die modifizierte Klasse zurück.

3. Nachdem Sie den Code hinzugefügt haben, speichern Sie die Datei `structure.py`. Das Speichern der Datei stellt sicher, dass Ihre Änderungen erhalten bleiben.

4. Nun müssen wir unsere Datei `stock.py` ändern, um diesen neuen Dekorator zu verwenden. Öffnen Sie die Datei `stock.py` in Ihrem Editor.

5. Aktualisieren Sie die Datei `stock.py`, um den `validate_attributes`-Dekorator zu verwenden. Ersetzen Sie den vorhandenen Code durch Folgendes:

```python
# stock.py

from structure import Structure, validate_attributes
from validate import String, PositiveInteger, PositiveFloat

@validate_attributes
class Stock(Structure):
    name = String()
    shares = PositiveInteger()
    price = PositiveFloat()

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, nshares):
        self.shares -= nshares
```

Beachten Sie die Änderungen, die wir vorgenommen haben:

- Wir haben den `@validate_attributes`-Dekorator direkt über der `Stock`-Klassendefinition hinzugefügt. Dies weist Python an, den `validate_attributes`-Dekorator auf die `Stock`-Klasse anzuwenden.
- Wir haben die explizite `_fields`-Deklaration entfernt, da der Dekorator dies automatisch übernimmt.
- Wir haben auch den Aufruf von `Stock.create_init()` entfernt, da der Dekorator die Erstellung der `__init__`-Methode übernimmt.

Dadurch ist die Klasse nun einfacher und sauberer. Der Dekorator kümmert sich um alle Details, die wir zuvor manuell erledigt haben.

6. Nachdem Sie diese Änderungen vorgenommen haben, müssen wir überprüfen, ob alles weiterhin wie erwartet funktioniert. Führen Sie die Tests erneut mit den folgenden Befehlen aus:

```bash
cd ~/project
python3 teststock.py
```

Wenn alles korrekt funktioniert, sollten Sie die folgende Ausgabe sehen:

```
.........
----------------------------------------------------------------------
Ran 9 tests in 0.001s

OK
```

Diese Ausgabe zeigt an, dass alle Tests erfolgreich bestanden wurden.

Testen wir unsere `Stock`-Klasse auch interaktiv. Führen Sie den folgenden Befehl im Terminal aus:

```bash
cd ~/project
python3 -c "from stock import Stock; s = Stock('GOOG', 100, 490.1); print(s); print(f'Cost: {s.cost}')"
```

Sie sollten die folgende Ausgabe sehen:

```
Stock('GOOG', 100, 490.1)
Cost: 49010.0
```

Großartig! Sie haben erfolgreich einen Klassendekorator implementiert, der unseren Code vereinfacht, indem er automatisch Felddeklarationen und Initialisierungen übernimmt. Dies macht unseren Code effizienter und einfacher zu warten.
