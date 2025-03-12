# Hinzufügen von Methoden-Argument-Validierung

In Python ist die Validierung von Daten ein wichtiger Bestandteil beim Schreiben robuster Code. In diesem Abschnitt gehen wir einen Schritt weiter und validieren automatisch die Argumente von Methoden. Die Datei `validate.py` enthält bereits einen `@validated`-Dekorator. Ein Dekorator in Python ist eine spezielle Funktion, die eine andere Funktion modifizieren kann. Der `@validated`-Dekorator hier kann die Argumente einer Funktion anhand ihrer Anmerkungen (annotations) überprüfen. Anmerkungen in Python sind eine Möglichkeit, Metadaten zu Funktionsparametern und Rückgabewerten hinzuzufügen.

Lassen Sie uns unseren Code ändern, um diesen Dekorator auf Methoden mit Anmerkungen anzuwenden:

1. Zunächst müssen wir verstehen, wie der `validated`-Dekorator funktioniert. Öffnen Sie die Datei `validate.py`, um sie zu überprüfen:

```bash
code ~/project/validate.py
```

Der `validated`-Dekorator nutzt Funktionsanmerkungen, um Argumente zu validieren. Bevor die Funktion ausgeführt wird, überprüft er jedes Argument anhand seines Anmerkungstyps. Beispielsweise, wenn ein Argument als Ganzzahl (integer) annotiert ist, stellt der Dekorator sicher, dass der übergebene Wert tatsächlich eine Ganzzahl ist.

2. Jetzt werden wir die Funktion `validate_attributes` in `structure.py` ändern, um annotierte Methoden mit dem `validated`-Dekorator zu umhüllen. Das bedeutet, dass alle Methoden mit Anmerkungen in der Klasse ihre Argumente automatisch validieren lassen. Öffnen Sie die Datei `structure.py`:

```bash
code ~/project/structure.py
```

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

Diese aktualisierte Funktion macht jetzt Folgendes:

1. Sie verarbeitet Validator-Deskriptoren wie zuvor. Validator-Deskriptoren werden verwendet, um Validierungsregeln für Klassenattribute zu definieren.
2. Sie findet alle Methoden mit Anmerkungen in der Klasse. Anmerkungen werden an Methodenparameter hinzugefügt, um den erwarteten Typ des Arguments anzugeben.
3. Sie wendet den `@validated`-Dekorator auf diese Methoden an. Dies stellt sicher, dass die an diese Methoden übergebenen Argumente gemäß ihren Anmerkungen validiert werden.

4. Speichern Sie die Datei nach diesen Änderungen. Das Speichern der Datei ist wichtig, da es sicherstellt, dass unsere Änderungen gespeichert werden und später verwendet werden können.

5. Jetzt aktualisieren wir die `sell`-Methode in der `Stock`-Klasse, um eine Anmerkung hinzuzufügen. Anmerkungen helfen dabei, den erwarteten Typ des Arguments anzugeben, der vom `@validated`-Dekorator für die Validierung verwendet wird. Öffnen Sie die Datei `stock.py`:

```bash
code ~/project/stock.py
```

6. Ändern Sie die `sell`-Methode, um eine Typanmerkung hinzuzufügen:

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

Die wichtigste Änderung ist das Hinzufügen von `: PositiveInteger` zum Parameter `nshares`. Dies sagt Python (und unserem `@validated`-Dekorator) aus, dass dieses Argument mit dem `PositiveInteger`-Validator validiert werden soll. Wenn wir also die `sell`-Methode aufrufen, muss das `nshares`-Argument eine positive Ganzzahl sein.

7. Führen Sie die Tests erneut aus, um sicherzustellen, dass alles noch funktioniert. Das Ausführen von Tests ist eine gute Möglichkeit, um sicherzustellen, dass unsere Änderungen keine bestehende Funktionalität zerstört haben.

```bash
cd ~/project
python3 teststock.py
```

Sie sollten alle Tests bestehen sehen:

```
.........
----------------------------------------------------------------------
Ran 9 tests in 0.001s

OK
```

8. Lassen Sie uns unsere neue Argumentvalidierung testen. Wir versuchen, die `sell`-Methode mit gültigen und ungültigen Argumenten aufzurufen, um zu sehen, ob die Validierung wie erwartet funktioniert.

```bash
cd ~/project
python3 -c "from stock import Stock; s = Stock('GOOG', 100, 490.1); s.sell(25); print(s); try: s.sell(-25); except Exception as e: print(f'Error: {e}')"
```

Sie sollten eine Ausgabe ähnlich der folgenden sehen:

```
Stock('GOOG', 75, 490.1)
Error: Bad Arguments
  nshares: must be >= 0
```

Dies zeigt, dass unsere Methoden-Argument-Validierung funktioniert! Der erste Aufruf von `sell(25)` ist erfolgreich, da `25` eine positive Ganzzahl ist. Aber der zweite Aufruf von `sell(-25)` schlägt fehl, da `-25` keine positive Ganzzahl ist.

Sie haben jetzt ein komplettes System implementiert für:

1. Die Validierung von Klassenattributen mit Deskriptoren. Deskriptoren werden verwendet, um Validierungsregeln für Klassenattribute zu definieren.
2. Das automatische Sammeln von Feldinformationen mit Klassen-Dekoratoren. Klassen-Dekorateure können das Verhalten einer Klasse ändern, wie z.B. das Sammeln von Feldinformationen.
3. Das Konvertieren von Zeilendaten in Instanzen. Dies ist nützlich, wenn man mit Daten aus externen Quellen arbeitet.
4. Die Validierung von Methodenargumenten mit Anmerkungen. Anmerkungen helfen dabei, den erwarteten Typ des Arguments für die Validierung anzugeben.

Dies zeigt die Stärke der Kombination von Deskriptoren und Dekoratoren in Python, um ausdrucksstarke, selbstvalidierende Klassen zu erstellen.
