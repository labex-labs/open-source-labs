# Anwenden von Dekoratoren durch Vererbung

In Schritt 2 haben wir einen Klassendekorator erstellt, der unseren Code vereinfacht. Ein Klassendekorator ist ein spezieller Funktionstyp, der eine Klasse als Argument nimmt und eine modifizierte Klasse zurückgibt. Es ist ein nützliches Werkzeug in Python, um Klassen Funktionalität hinzuzufügen, ohne ihren ursprünglichen Code zu ändern. Wir müssen jedoch weiterhin explizit den `@validate_attributes`-Dekorator auf jede Klasse anwenden. Das bedeutet, dass wir jedes Mal, wenn wir eine neue Klasse erstellen, die eine Validierung benötigt, daran denken müssen, diesen Dekorator hinzuzufügen, was etwas umständlich sein kann.

Wir können dies weiter verbessern, indem wir den Dekorator automatisch durch Vererbung anwenden. Vererbung ist ein grundlegendes Konzept in der objektorientierten Programmierung, bei dem eine Unterklasse Attribute und Methoden von einer Oberklasse erben kann. Die `__init_subclass__`-Methode von Python wurde in Python 3.6 eingeführt, um Oberklassen die Anpassung der Initialisierung von Unterklassen zu ermöglichen. Das bedeutet, dass die Oberklasse einige Aktionen auf die Unterklasse ausführen kann, wenn diese erstellt wird. Wir können diese Funktion nutzen, um unseren Dekorator automatisch auf jede Klasse anzuwenden, die von `Structure` erbt.

Lassen Sie uns dies implementieren:

1. Öffnen Sie die Datei `structure.py` in Ihrem Editor. Diese Datei enthält die Definition der `Structure`-Klasse, und wir werden sie ändern, um die `__init_subclass__`-Methode zu verwenden.

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

Die `__init_subclass__`-Methode ist eine Klassenmethode, was bedeutet, dass sie auf der Klasse selbst und nicht auf einer Instanz der Klasse aufgerufen werden kann. Wenn eine Unterklasse von `Structure` erstellt wird, wird diese Methode automatisch aufgerufen. Innerhalb dieser Methode rufen wir den `validate_attributes`-Dekorator auf der Unterklasse `cls` auf. Auf diese Weise erhalten alle Unterklassen von `Structure` automatisch das Validierungsverhalten.

3. Speichern Sie die Datei.

Nachdem Sie Änderungen an der Datei `structure.py` vorgenommen haben, müssen wir sie speichern, damit die Änderungen angewendet werden.

4. Aktualisieren wir nun unsere Datei `stock.py`, um diese neue Funktion zu nutzen. Öffnen Sie die Datei `stock.py` in Ihrem Editor, um sie zu ändern. Diese Datei enthält die Definition der `Stock`-Klasse, und wir werden sie von der `Structure`-Klasse erben lassen, um die automatische Anwendung des Dekorators zu nutzen.

5. Ändern Sie die Datei `stock.py`, um den expliziten Dekorator zu entfernen:

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

- Den Import von `validate_attributes` entfernt haben, da wir ihn nicht mehr explizit importieren müssen, da der Dekorator automatisch durch Vererbung angewendet wird.
- Den `@validate_attributes`-Dekorator entfernt haben, da die `__init_subclass__`-Methode in der `Structure`-Klasse für die Anwendung zuständig ist.
- Der Code verlässt sich nun ausschließlich auf die Vererbung von `Structure`, um das Validierungsverhalten zu erhalten.

6. Führen Sie die Tests erneut aus, um zu überprüfen, ob alles noch funktioniert:

```bash
cd ~/project
python3 teststock.py
```

Das Ausführen der Tests ist wichtig, um sicherzustellen, dass unsere Änderungen nichts kaputt gemacht haben. Wenn alle Tests bestanden werden, bedeutet dies, dass die automatische Anwendung des Dekorators durch Vererbung korrekt funktioniert.

Sie sollten sehen, dass alle Tests bestanden werden:

```
.........
----------------------------------------------------------------------
Ran 9 tests in 0.001s

OK
```

Testen wir unsere `Stock`-Klasse erneut, um sicherzustellen, dass sie wie erwartet funktioniert:

```bash
cd ~/project
python3 -c "from stock import Stock; s = Stock('GOOG', 100, 490.1); print(s); print(f'Cost: {s.cost}')"
```

Dieser Befehl erstellt eine Instanz der `Stock`-Klasse und gibt ihre Darstellung und die Kosten aus. Wenn die Ausgabe wie erwartet ist, bedeutet dies, dass die `Stock`-Klasse mit der automatischen Dekoratoranwendung korrekt funktioniert.

Ausgabe:

```
Stock('GOOG', 100, 490.1)
Cost: 49010.0
```

Diese Implementierung ist noch sauberer! Durch die Verwendung von `__init_subclass__` haben wir die Notwendigkeit eliminiert, Dekoratoren explizit anzuwenden. Jede Klasse, die von `Structure` erbt, erhält automatisch das Validierungsverhalten.
