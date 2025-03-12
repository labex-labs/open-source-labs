# Erstellen eines Klassen-Dekorateurs zur Validierung

Im vorherigen Schritt hat unsere Implementierung funktioniert, aber es gab eine Redundanz. Wir mussten sowohl das `_fields`-Tupel als auch die Deskriptor-Attribute angeben. Dies ist nicht sehr effizient, und wir können es verbessern. In Python sind Klassen-Dekorateure (class decorators) ein leistungsstarkes Werkzeug, das uns helfen kann, diesen Prozess zu vereinfachen. Ein Klassen-Dekorator ist eine Funktion, die eine Klasse als Argument nimmt, sie auf irgendeine Weise modifiziert und dann die modifizierte Klasse zurückgibt. Indem wir einen Klassen-Dekorator verwenden, können wir automatisch Feldinformationen aus den Deskriptoren extrahieren, was unseren Code sauberer und wartbarer machen wird.

Lassen Sie uns einen Klassen-Dekorator erstellen, um unseren Code zu vereinfachen. Hier sind die Schritte, die Sie befolgen müssen:

1. Öffnen Sie zunächst die Datei `structure.py`. Sie können den folgenden Befehl im Terminal verwenden:

```bash
code ~/project/structure.py
```

Dieser Befehl wird die Datei `structure.py` in Ihrem Code-Editor öffnen.

2. Fügen Sie als Nächstes den folgenden Code ganz oben in die Datei `structure.py` ein, direkt nach allen Import-Anweisungen. Dieser Code definiert unseren Klassen-Dekorator:

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

Lassen Sie uns analysieren, was dieser Dekorator tut:

- Zunächst erstellt er eine leere Liste namens `validators`. Dann iteriert er über alle Attribute der Klasse mithilfe von `vars(cls).items()`. Wenn ein Attribut eine Instanz der `Validator`-Klasse ist, fügt er dieses Attribut der `validators`-Liste hinzu.
- Danach setzt er das `_fields`-Attribut der Klasse. Er erstellt eine Liste von Namen aus den Validatoren in der `validators`-Liste und weist sie `cls._fields` zu.
- Schließlich ruft er die `create_init()`-Methode der Klasse auf, um die `__init__`-Methode zu generieren, und gibt dann die modifizierte Klasse zurück.

3. Sobald Sie den Code hinzugefügt haben, speichern Sie die Datei `structure.py`. Das Speichern der Datei stellt sicher, dass Ihre Änderungen beibehalten werden.

4. Jetzt müssen wir die Datei `stock.py` ändern, um diesen neuen Dekorator zu verwenden. Öffnen Sie die Datei `stock.py` mit dem folgenden Befehl:

```bash
code ~/project/stock.py
```

5. Aktualisieren Sie die Datei `stock.py`, um den `validate_attributes`-Dekorator zu verwenden. Ersetzen Sie den vorhandenen Code durch den folgenden:

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

- Wir haben den `@validate_attributes`-Dekorator direkt über der Definition der `Stock`-Klasse hinzugefügt. Dies teilt Python mit, den `validate_attributes`-Dekorator auf die `Stock`-Klasse anzuwenden.
- Wir haben die explizite `_fields`-Deklaration entfernt, da der Dekorator dies automatisch erledigt.
- Wir haben auch den Aufruf von `Stock.create_init()` entfernt, da der Dekorator die Erstellung der `__init__`-Methode übernimmt.

Infolgedessen ist die Klasse jetzt einfacher und sauberer. Der Dekorator kümmert sich um alle Details, die wir früher manuell bearbeitet haben.

6. Nach diesen Änderungen müssen wir überprüfen, ob alles noch wie erwartet funktioniert. Führen Sie die Tests erneut mit den folgenden Befehlen aus:

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

Lassen Sie uns auch unsere `Stock`-Klasse interaktiv testen. Führen Sie den folgenden Befehl im Terminal aus:

```bash
cd ~/project
python3 -c "from stock import Stock; s = Stock('GOOG', 100, 490.1); print(s); print(f'Cost: {s.cost}')"
```

Sie sollten die folgende Ausgabe sehen:

```
Stock('GOOG', 100, 490.1)
Cost: 49010.0
```

Toll! Sie haben erfolgreich einen Klassen-Dekorator implementiert, der unseren Code vereinfacht, indem er Felddeklarationen und Initialisierung übernimmt. Dies macht unseren Code effizienter und leichter wartbar.
