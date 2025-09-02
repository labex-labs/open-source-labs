# Hinzufügen von Validierungsfunktionalität für Methodenargumente

In Python ist die Validierung von Daten ein wichtiger Bestandteil der Erstellung robuster Codes. In diesem Abschnitt erweitern wir unsere Validierung, indem wir Methodenargumente automatisch validieren. Die Datei `validate.py` enthält bereits einen `@validated`-Dekorator. Ein Dekorator in Python ist eine spezielle Funktion, die eine andere Funktion modifizieren kann. Der `@validated`-Dekorator hier kann Funktionsargumente anhand ihrer Annotationen überprüfen. Annotationen in Python sind eine Möglichkeit, Metadaten zu Funktionsparametern und Rückgabewerten hinzuzufügen.

Lassen Sie uns unseren Code ändern, um diesen Dekorator auf Methoden mit Annotationen anzuwenden:

1. Zuerst müssen wir verstehen, wie der `validated`-Dekorator funktioniert. Öffnen Sie die Datei `validate.py` in Ihrem Editor, um sie zu überprüfen.

Der `validated`-Dekorator verwendet Funktionsannotationen zur Validierung von Argumenten. Bevor die Funktion ausgeführt werden kann, erstellt er für jeden annotierten Parameter eine Instanz der Validator-Klasse und ruft die `validate`-Methode auf, um das Argument zu überprüfen. Wenn ein Argument beispielsweise mit `PositiveInteger` annotiert ist, erstellt der Dekorator eine `PositiveInteger`-Instanz und validiert, dass der übergebene Wert tatsächlich eine positive Ganzzahl ist. Wenn die Validierung fehlschlägt, sammelt er alle Fehler und löst einen `TypeError` mit detaillierten Fehlermeldungen aus.

2. Nun ändern wir die Funktion `validate_attributes` in `structure.py`, um annotierte Methoden mit dem `validated`-Dekorator zu umschließen. Das bedeutet, dass jede Methode mit Annotationen in der Klasse ihre Argumente automatisch validiert bekommt. Öffnen Sie die Datei `structure.py` in Ihrem Editor.

3. Aktualisieren Sie die Funktion `validate_attributes`:

```python
def validate_attributes(cls):
    """
    Class decorator that:
    1. Extracts Validator instances and builds _fields and _types lists
    2. Applies @validated decorator to methods with annotations
    """
    # Import the validated decorator
    from validate import validated

    # Process validator descriptors
    validators = []
    for name, val in vars(cls).items():
        if isinstance(val, Validator):
            validators.append(val)

    # Set _fields based on validator names
    cls._fields = [val.name for val in validators]

    # Set _types based on validator expected_types
    cls._types = [getattr(val, 'expected_type', lambda x: x) for val in validators]

    # Apply @validated decorator to methods with annotations
    for name, val in vars(cls).items():
        if callable(val) and hasattr(val, '__annotations__'):
            setattr(cls, name, validated(val))

    # Create initialization method
    cls.create_init()

    return cls
```

Diese aktualisierte Funktion führt nun Folgendes aus:

1. Sie verarbeitet wie bisher Validator-Deskriptoren. Validator-Deskriptoren werden verwendet, um Validierungsregeln für Klassenattribute zu definieren.
2. Sie findet alle Methoden mit Annotationen in der Klasse. Annotationen werden zu Methodenparametern hinzugefügt, um den erwarteten Typ des Arguments anzugeben.
3. Sie wendet den `@validated`-Dekorator auf diese Methoden an. Dies stellt sicher, dass die an diese Methoden übergebenen Argumente gemäß ihren Annotationen validiert werden.

4. Speichern Sie die Datei nach diesen Änderungen. Das Speichern der Datei ist wichtig, da es sicherstellt, dass unsere Änderungen gespeichert und später verwendet werden können.

5. Aktualisieren wir nun die `sell`-Methode in der `Stock`-Klasse, um eine Annotation hinzuzufügen. Annotationen helfen bei der Angabe des erwarteten Typs des Arguments, der vom `@validated`-Dekorator zur Validierung verwendet wird. Öffnen Sie die Datei `stock.py` in Ihrem Editor.

6. Ändern Sie die `sell`-Methode, um eine Typannotation hinzuzufügen:

```python
# stock.py

from structure import Structure
from validate import String, PositiveInteger, PositiveFloat

class Stock(Structure):
    name = String()
    shares = PositiveInteger()
    price = PositiveFloat()

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, nshares: PositiveInteger):
        self.shares -= nshares
```

Die wichtige Änderung ist das Hinzufügen von `: PositiveInteger` zum Parameter `nshares`. Dies teilt Python (und unserem `@validated`-Dekorator) mit, dieses Argument mit dem `PositiveInteger`-Validator zu validieren. Wenn wir also die `sell`-Methode aufrufen, muss das Argument `nshares` eine positive Ganzzahl sein.

7. Führen Sie die Tests erneut aus, um zu überprüfen, ob alles noch funktioniert. Das Ausführen von Tests ist eine gute Möglichkeit, sicherzustellen, dass unsere Änderungen keine bestehende Funktionalität beeinträchtigt haben.

```bash
cd ~/project
python3 teststock.py
```

Sie sollten sehen, dass alle Tests bestanden werden:

```
.........
----------------------------------------------------------------------
Ran 9 tests in 0.001s

OK
```

8. Testen wir unsere neue Argumentvalidierung. Wir werden versuchen, die `sell`-Methode mit gültigen und ungültigen Argumenten aufzurufen, um zu sehen, ob die Validierung wie erwartet funktioniert.

```bash
cd ~/project
python3 -c "
from stock import Stock
s = Stock('GOOG', 100, 490.1)
s.sell(25)
print(s)
try:
    s.sell(-25)
except Exception as e:
    print(f'Error: {e}')
"
```

Sie sollten eine Ausgabe ähnlich der folgenden sehen:

```
Stock('GOOG', 75, 490.1)
Error: Bad Arguments
  nshares: nshares must be >= 0
```

Dies zeigt, dass unsere Methodenargumentvalidierung funktioniert! Der erste Aufruf von `sell(25)` ist erfolgreich, da `25` eine positive Ganzzahl ist. Der zweite Aufruf von `sell(-25)` schlägt jedoch fehl, da `-25` keine positive Ganzzahl ist.

Sie haben nun ein vollständiges System implementiert für:

1. Validierung von Klassenattributen mithilfe von Deskriptoren. Deskriptoren werden verwendet, um Validierungsregeln für Klassenattribute zu definieren.
2. Automatische Sammlung von Feldinformationen mithilfe von Klassendekoratoren. Klassendekoratoren können das Verhalten einer Klasse modifizieren, z. B. die Sammlung von Feldinformationen.
3. Konvertierung von Zeilendaten in Instanzen. Dies ist nützlich, wenn mit Daten aus externen Quellen gearbeitet wird.
4. Validierung von Methodenargumenten mithilfe von Annotationen. Annotationen helfen bei der Angabe des erwarteten Typs des Arguments für die Validierung.

Dies demonstriert die Leistungsfähigkeit der Kombination von Deskriptoren und Dekoratoren in Python, um ausdrucksstarke, sich selbst validierende Klassen zu erstellen.
