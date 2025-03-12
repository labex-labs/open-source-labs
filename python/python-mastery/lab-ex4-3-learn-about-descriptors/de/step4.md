# Verbesserung der Descriptor-Implementierung

In diesem Schritt werden wir unsere Descriptor-Implementierung verbessern. Sie haben vielleicht bemerkt, dass wir in einigen Fällen Namen redundant angegeben haben. Dies kann unseren Code etwas unübersichtlich und schwieriger zu warten machen. Um dieses Problem zu lösen, verwenden wir die `__set_name__`-Methode, eine nützliche Funktion, die in Python 3.6 eingeführt wurde.

Die `__set_name__`-Methode wird automatisch aufgerufen, wenn die Klasse definiert wird. Ihre Hauptaufgabe ist es, den Namen des Descriptors für uns festzulegen, sodass wir dies nicht jedes Mal manuell tun müssen. Dies macht unseren Code sauberer und effizienter.

Jetzt aktualisieren wir Ihre `validate.py`-Datei, um die `__set_name__`-Methode einzubeziehen. So wird der aktualisierte Code aussehen:

```python
# validate.py

class Validator:
    def __init__(self, name=None):
        self.name = name

    def __set_name__(self, cls, name):
        # This gets called when the class is defined
        # It automatically sets the name of the descriptor
        if self.name is None:
            self.name = name

    @classmethod
    def check(cls, value):
        return value

    def __set__(self, instance, value):
        instance.__dict__[self.name] = self.check(value)


class String(Validator):
    expected_type = str

    @classmethod
    def check(cls, value):
        if not isinstance(value, cls.expected_type):
            raise TypeError(f'Expected {cls.expected_type}')
        return value


class PositiveInteger(Validator):
    expected_type = int

    @classmethod
    def check(cls, value):
        if not isinstance(value, cls.expected_type):
            raise TypeError(f'Expected {cls.expected_type}')
        if value < 0:
            raise ValueError('Expected a positive value')
        return value


class PositiveFloat(Validator):
    expected_type = float

    @classmethod
    def check(cls, value):
        if not isinstance(value, (int, float)):
            raise TypeError('Expected a number')
        if value < 0:
            raise ValueError('Expected a positive value')
        return float(value)
```

Im obigen Code überprüft die `__set_name__`-Methode in der `Validator`-Klasse, ob das `name`-Attribut `None` ist. Wenn dies der Fall ist, setzt es das `name` auf den tatsächlichen Attributnamen, der in der Klassendefinition verwendet wird. Auf diese Weise müssen wir den Namen nicht explizit angeben, wenn wir Instanzen der Descriptor-Klassen erstellen.

Jetzt, da wir die `validate.py`-Datei aktualisiert haben, können wir eine verbesserte Version unserer `Stock`-Klasse erstellen. Diese neue Version erfordert es uns nicht mehr, die Namen redundant anzugeben. Hier ist der Code für die verbesserte `Stock`-Klasse:

```python
# improved_stock.py

from validate import String, PositiveInteger, PositiveFloat

class Stock:
    name = String()  # No need to specify 'name' anymore
    shares = PositiveInteger()
    price = PositiveFloat()

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def cost(self):
        return self.shares * self.price

    def sell(self, amount):
        self.shares -= amount

    def __repr__(self):
        return f'Stock({self.name!r}, {self.shares!r}, {self.price!r})'
```

In dieser `Stock`-Klasse erstellen wir einfach Instanzen der `String`, `PositiveInteger` und `PositiveFloat` Descriptor-Klassen, ohne die Namen anzugeben. Die `__set_name__`-Methode in der `Validator`-Klasse kümmert sich automatisch um das Festlegen der Namen.

Lassen Sie uns unsere verbesserte `Stock`-Klasse testen. Öffnen Sie zunächst Ihr Terminal und navigieren Sie zum Projektverzeichnis. Führen Sie dann die `improved_stock.py`-Datei im interaktiven Modus aus. Hier sind die Befehle dazu:

```bash
cd ~/project
python3 -i improved_stock.py
```

Sobald Sie in der interaktiven Python-Sitzung sind, können Sie die folgenden Befehle ausprobieren, um die Funktionalität der `Stock`-Klasse zu testen:

```python
s = Stock('GOOG', 100, 490.10)
print(s.name)    # Should return 'GOOG'
print(s.shares)  # Should return 100
print(s.price)   # Should return 490.1

# Try changing values
s.shares = 75
print(s.shares)  # Should return 75

# Try invalid values
try:
    s.shares = '75'  # Should raise TypeError
except TypeError as e:
    print(f"Error: {e}")

try:
    s.price = -10.5  # Should raise ValueError
except ValueError as e:
    print(f"Error: {e}")

exit()
```

Diese Befehle erstellen eine Instanz der `Stock`-Klasse, geben ihre Attribute aus, ändern den Wert eines Attributs und versuchen dann, ungültige Werte zu setzen, um zu sehen, ob die entsprechenden Fehler ausgelöst werden.

Die `__set_name__`-Methode legt automatisch den Namen des Descriptors fest, wenn die Klasse definiert wird. Dies macht Ihren Code sauberer und weniger redundant, da Sie den Attributnamen nicht mehr zweimal angeben müssen.

Diese Verbesserung zeigt, wie sich das Descriptor-Protokoll von Python weiterentwickelt und es einfacher macht, sauberen und wartbaren Code zu schreiben.
