# Erstellen der StructureMeta-Metaklasse

Jetzt sprechen wir darüber, was wir als Nächstes tun werden. Wir haben einen Weg gefunden, alle Validator-Typen zu sammeln. Unser nächster Schritt besteht darin, eine Metaklasse zu erstellen. Aber was genau ist eine Metaklasse? In Python ist eine Metaklasse eine besondere Art von Klasse. Ihre Instanzen sind selbst Klassen. Das bedeutet, dass eine Metaklasse steuern kann, wie eine Klasse erstellt wird. Sie kann den Namensraum verwalten, in dem die Klassenattribute definiert werden.

In unserer Situation möchten wir eine Metaklasse erstellen, die die Validator-Typen verfügbar macht, wenn wir eine `Structure`-Unterklasse definieren. Wir möchten nicht jedes Mal diese Validator-Typen explizit importieren müssen.

Beginnen wir damit, die Datei `structure.py` erneut zu öffnen. Sie können den folgenden Befehl verwenden, um sie zu öffnen:

```bash
code structure.py
```

Sobald die Datei geöffnet ist, müssen wir etwas Code oben in der Datei, vor der Definition der `Structure`-Klasse, hinzufügen. Dieser Code wird unsere Metaklasse definieren.

```python
from validate import Validator
from collections import ChainMap

class StructureMeta(type):
    @classmethod
    def __prepare__(meta, clsname, bases):
        """Prepare the namespace for the class being defined"""
        return ChainMap({}, Validator.validators)

    @staticmethod
    def __new__(meta, name, bases, methods):
        """Create the new class using only the local namespace"""
        methods = methods.maps[0]  # Extract the local namespace
        return super().__new__(meta, name, bases, methods)
```

Jetzt, da wir die Metaklasse definiert haben, müssen wir die `Structure`-Klasse modifizieren, um sie zu verwenden. Auf diese Weise profitiert jede Klasse, die von `Structure` erbt, von der Funktionalität der Metaklasse.

```python
class Structure(metaclass=StructureMeta):
    _fields = []

    def __init__(self, *args, **kwargs):
        if len(args) > len(self._fields):
            raise TypeError(f'Expected {len(self._fields)} arguments')

        # Set all of the positional arguments
        for name, val in zip(self._fields, args):
            setattr(self, name, val)

        # Set the remaining keyword arguments
        for name, val in kwargs.items():
            if name not in self._fields:
                raise TypeError(f'Invalid argument: {name}')
            setattr(self, name, val)

    def __repr__(self):
        values = [getattr(self, name) for name in self._fields]
        args_str = ','.join(repr(val) for val in values)
        return f'{type(self).__name__}({args_str})'
```

Lassen Sie uns analysieren, was dieser Code tut:

1. Die `__prepare__()`-Methode ist eine spezielle Methode in Python. Sie wird aufgerufen, bevor die Klasse erstellt wird. Ihre Aufgabe besteht darin, den Namensraum vorzubereiten, in dem die Klassenattribute definiert werden. Wir verwenden hier `ChainMap`. `ChainMap` ist ein nützliches Werkzeug, das ein geschichtetes Wörterbuch erstellt. In unserem Fall enthält es unsere Validator-Typen, wodurch sie im Klassen-Namensraum zugänglich sind.

2. Die `__new__()`-Methode ist für die Erstellung der neuen Klasse verantwortlich. Wir extrahieren nur den lokalen Namensraum, der das erste Wörterbuch in der `ChainMap` ist. Wir verwerfen das Validator-Wörterbuch, da wir die Validator-Typen bereits im Namensraum verfügbar gemacht haben.

Mit dieser Einrichtung hat jede Klasse, die von `Structure` erbt, Zugang zu allen Validator-Typen, ohne dass es erforderlich ist, sie explizit zu importieren.

Jetzt testen wir unsere Implementierung. Wir erstellen eine `Stock`-Klasse, die von unserer erweiterten `Structure`-Basisklasse erbt.

```bash
cat > stock.py << EOF
from structure import Structure

class Stock(Structure):
    name = String()
    shares = PositiveInteger()
    price = PositiveFloat()

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, nshares: PositiveInteger):
        self.shares -= nshares
EOF
```

Wenn unsere Metaklasse korrekt funktioniert, sollten wir in der Lage sein, die `Stock`-Klasse zu definieren, ohne die Validator-Typen zu importieren. Dies liegt daran, dass die Metaklasse sie bereits im Namensraum verfügbar gemacht hat.
