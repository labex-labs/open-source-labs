# Implementierung der erweiterten Initialisierung in der `Structure`-Klasse

Wir haben gerade zwei leistungsstarke Techniken zum Zugriff auf Funktionsargumente gelernt. Jetzt werden wir diese Techniken nutzen, um unsere `Structure`-Klasse zu aktualisieren. Zunächst verstehen wir, warum wir dies tun. Diese Techniken machen unsere Klasse flexibler und einfacher zu verwenden, insbesondere wenn es um verschiedene Argumenttypen geht.

Öffnen Sie die Datei `structure.py` im Code-Editor. Sie können dies tun, indem Sie die folgenden Befehle im Terminal ausführen. Der `cd`-Befehl wechselt das Verzeichnis in den Projektordner, und der `code`-Befehl öffnet die Datei `structure.py` im Code-Editor.

```bash
cd ~/project
code structure.py
```

Ersetzen Sie den Inhalt der Datei durch den folgenden Code. Dieser Code definiert eine `Structure`-Klasse mit mehreren Methoden. Gehen wir durch jeden Teil, um zu verstehen, was er tut.

```python
import sys

class Structure:
    _fields = ()

    @staticmethod
    def _init():
        # Get the caller's frame (the __init__ method that called this)
        frame = sys._getframe(1)

        # Get the local variables from that frame
        locs = frame.f_locals

        # Extract self and set other variables as attributes
        self = locs.pop('self')
        for name, val in locs.items():
            setattr(self, name, val)

    def __repr__(self):
        values = ', '.join(f'{name}={getattr(self, name)!r}' for name in self._fields)
        return f'{type(self).__name__}({values})'

    def __setattr__(self, name, value):
        if name.startswith('_') or name in self._fields:
            super().__setattr__(name, value)
        else:
            raise AttributeError(f'{type(self).__name__!r} has no attribute {name!r}')
```

Hier ist, was wir im Code getan haben:

1. Wir haben die alte `__init__()`-Methode entfernt. Da Unterklassen ihre eigenen `__init__`-Methoden definieren werden, benötigen wir die alte nicht mehr.
2. Wir haben eine neue statische `_init()`-Methode hinzugefügt. Diese Methode nutzt die Frame-Inspektion, um automatisch alle Parameter als Attribute zu erfassen und zu setzen. Die Frame-Inspektion ermöglicht es uns, auf die lokalen Variablen der aufrufenden Methode zuzugreifen.
3. Wir haben die `__repr__()`-Methode beibehalten. Diese Methode liefert eine schöne String-Repräsentation des Objekts, die für das Debugging und das Ausgeben nützlich ist.
4. Wir haben eine `__setattr__()`-Methode hinzugefügt. Diese Methode erzwingt die Attributvalidierung und stellt sicher, dass nur gültige Attribute für das Objekt festgelegt werden können.

Jetzt aktualisieren wir die `Stock`-Klasse. Öffnen Sie die Datei `stock.py` mit dem folgenden Befehl:

```bash
code stock.py
```

Ersetzen Sie ihren Inhalt durch den folgenden Code:

```python
from structure import Structure

class Stock(Structure):
    _fields = ('name', 'shares', 'price')

    def __init__(self, name, shares, price):
        self._init()  # This magically captures and sets all parameters!

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, nshares):
        self.shares -= nshares
```

Der wichtigste Unterschied hier ist, dass unsere `__init__`-Methode jetzt `self._init()` aufruft, anstatt jedes Attribut manuell zu setzen. Die `_init()`-Methode nutzt die Frame-Inspektion, um automatisch alle Parameter als Attribute zu erfassen und zu setzen. Dies macht den Code kompakter und leichter zu warten.

Lassen Sie uns unsere Implementierung testen, indem wir die Unittests ausführen. Die Unittests helfen uns, sicherzustellen, dass unser Code wie erwartet funktioniert. Führen Sie die folgenden Befehle im Terminal aus:

```bash
cd ~/project
python3 teststock.py
```

Sie sollten sehen, dass alle Tests bestanden werden, einschließlich des Tests für Schlüsselwortargumente, der zuvor fehlgeschlagen ist. Dies bedeutet, dass unsere Implementierung korrekt funktioniert.

Lassen Sie uns auch die Hilfedokumentation für unsere `Stock`-Klasse überprüfen. Die Hilfedokumentation liefert Informationen über die Klasse und ihre Methoden. Führen Sie den folgenden Befehl im Terminal aus:

```bash
python3 -c "from stock import Stock; help(Stock)"
```

Jetzt sollten Sie eine korrekte Signatur für die `__init__`-Methode sehen, die alle Parameternamen anzeigt. Dies erleichtert es anderen Entwicklern, zu verstehen, wie die Klasse verwendet werden kann.

Schließlich testen wir interaktiv, ob Schlüsselwortargumente wie erwartet funktionieren. Führen Sie den folgenden Befehl im Terminal aus:

```bash
python3 -c "from stock import Stock; s = Stock(name='GOOG', shares=100, price=490.1); print(s)"
```

Sie sollten sehen, dass das `Stock`-Objekt ordnungsgemäß mit den angegebenen Attributen erstellt wird. Dies bestätigt, dass unser Klasseninitialisierungssystem Schlüsselwortargumente unterstützt.

Mit dieser Implementierung haben wir ein viel flexibleres und benutzerfreundlicheres Klasseninitialisierungssystem erreicht, das:

1. Die richtigen Funktionssignaturen in der Dokumentation beibehält, was es Entwicklern erleichtert, zu verstehen, wie die Klasse verwendet wird.
2. Sowohl Positions- als auch Schlüsselwortargumente unterstützt, was mehr Flexibilität bei der Objekterstellung bietet.
3. Minimalen Boilerplate-Code in Unterklassen erfordert, wodurch die Menge an zu schreibendem Code reduziert wird.
