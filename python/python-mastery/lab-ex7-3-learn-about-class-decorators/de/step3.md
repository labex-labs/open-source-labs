# Anwenden von Dekoratoren über Vererbung

In Schritt 2 haben wir einen Klassen-Dekorator (class decorator) erstellt, der unseren Code vereinfacht. Ein Klassen-Dekorator ist eine spezielle Art von Funktion, die eine Klasse als Argument nimmt und eine modifizierte Klasse zurückgibt. Es ist ein nützliches Werkzeug in Python, um Klassen Funktionalität hinzuzufügen, ohne ihren ursprünglichen Code zu ändern. Allerdings müssen wir immer noch den `@validate_attributes`-Dekorator explizit auf jede Klasse anwenden. Das bedeutet, dass jedes Mal, wenn wir eine neue Klasse erstellen, die Validierung benötigt, wir daran denken müssen, diesen Dekorator hinzuzufügen, was etwas umständlich sein kann.

Wir können dies weiter verbessern, indem wir den Dekorator automatisch über Vererbung anwenden. Vererbung ist ein grundlegendes Konzept in der objektorientierten Programmierung, bei dem eine Unterklasse (subclass) Attribute und Methoden von einer Elternklasse (parent class) erben kann. Python's `__init_subclass__`-Methode wurde in Python 3.6 eingeführt, um es Elternklassen zu ermöglichen, die Initialisierung von Unterklassen anzupassen. Das bedeutet, dass wenn eine Unterklasse erstellt wird, die Elternklasse einige Aktionen an ihr ausführen kann. Wir können diese Funktion nutzen, um unseren Dekorator automatisch auf jede Klasse anzuwenden, die von `Structure` erbt.

Lassen Sie uns dies implementieren:

1. Öffnen Sie die Datei `structure.py`:

```bash
code ~/project/structure.py
```

Hier verwenden wir den `code`-Befehl, um die Datei `structure.py` in einem Code-Editor zu öffnen. Diese Datei enthält die Definition der `Structure`-Klasse, und wir werden sie ändern, um die `__init_subclass__`-Methode zu verwenden.

2. Fügen Sie die `__init_subclass__`-Methode zur `Structure`-Klasse hinzu:

```python
class Structure:
    _fields = ()
    _types = ()

    def __init__(self, *args):
        if len(args) != len(self._fields):
            raise TypeError(f'Expected {len(self._fields)} arguments')
        for name, val in zip(self._fields, args):
            setattr(self, name, val)

    def __repr__(self):
        values = ', '.join(repr(getattr(self, name)) for name in self._fields)
        return f'{type(self).__name__}({values})'

    @classmethod
    def create_init(cls):
        '''
        Create an __init__ method from _fields
        '''
        body = 'def __init__(self, %s):\n' % ', '.join(cls._fields)
        for name in cls._fields:
            body += f'    self.{name} = {name}\n'

        # Execute the function creation code
        namespace = {}
        exec(body, namespace)
        setattr(cls, '__init__', namespace['__init__'])

    @classmethod
    def __init_subclass__(cls):
        validate_attributes(cls)
```

Die `__init_subclass__`-Methode ist eine Klassenmethode (class method), was bedeutet, dass sie auf die Klasse selbst und nicht auf eine Instanz der Klasse aufgerufen werden kann. Wenn eine Unterklasse von `Structure` erstellt wird, wird diese Methode automatisch aufgerufen. Innerhalb dieser Methode rufen wir den `validate_attributes`-Dekorator auf die Unterklasse `cls` auf. Auf diese Weise wird jedes Mal, wenn eine Unterklasse von `Structure` erstellt wird, automatisch das Validierungsverhalten hinzugefügt.

3. Speichern Sie die Datei.

Nachdem wir die Datei `structure.py` geändert haben, müssen wir sie speichern, damit die Änderungen übernommen werden.

4. Jetzt aktualisieren wir unsere `stock.py`-Datei, um diese neue Funktion zu nutzen:

```bash
code ~/project/stock.py
```

Wir öffnen die Datei `stock.py`, um sie zu ändern. Diese Datei enthält die Definition der `Stock`-Klasse, und wir werden sie so ändern, dass sie von der `Structure`-Klasse erbt, um die automatische Anwendung des Dekorators zu nutzen.

5. Ändern Sie die `stock.py`-Datei, um den expliziten Dekorator zu entfernen:

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

    def sell(self, nshares):
        self.shares -= nshares
```

Beachten Sie, dass wir:

- Den Import von `validate_attributes` entfernt haben, da wir ihn nicht mehr explizit importieren müssen, da der Dekorator automatisch über Vererbung angewendet wird.
- Den `@validate_attributes`-Dekorator entfernt haben, da die `__init_subclass__`-Methode in der `Structure`-Klasse die Anwendung übernimmt.
- Der Code verlässt sich jetzt ausschließlich auf die Vererbung von `Structure`, um das Validierungsverhalten zu erhalten.

6. Führen Sie die Tests erneut aus, um zu überprüfen, ob alles noch funktioniert:

```bash
cd ~/project
python3 teststock.py
```

Das Ausführen der Tests ist wichtig, um sicherzustellen, dass unsere Änderungen nichts kaputt gemacht haben. Wenn alle Tests bestanden werden, bedeutet das, dass die automatische Anwendung des Dekorators über Vererbung korrekt funktioniert.

Sie sollten alle Tests bestehen sehen:

```
.........
----------------------------------------------------------------------
Ran 9 tests in 0.001s

OK
```

Lassen Sie uns unsere `Stock`-Klasse erneut testen, um sicherzustellen, dass sie wie erwartet funktioniert:

```bash
cd ~/project
python3 -c "from stock import Stock; s = Stock('GOOG', 100, 490.1); print(s); print(f'Cost: {s.cost}')"
```

Dieser Befehl erstellt eine Instanz der `Stock`-Klasse und gibt ihre Darstellung und die Kosten aus. Wenn die Ausgabe wie erwartet ist, bedeutet das, dass die `Stock`-Klasse mit der automatischen Anwendung des Dekorators korrekt funktioniert.

Ausgabe:

```
Stock('GOOG', 100, 490.1)
Cost: 49010.0
```

Diese Implementierung ist noch sauberer! Indem wir `__init_subclass__` verwenden, haben wir die Notwendigkeit, Dekorateure explizit anzuwenden, beseitigt. Jede Klasse, die von `Structure` erbt, erhält automatisch das Validierungsverhalten.
