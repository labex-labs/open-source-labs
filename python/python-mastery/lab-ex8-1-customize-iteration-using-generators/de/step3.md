# Verbessern von Klassen mit Iterationsfähigkeiten

Jetzt haben wir unsere `Structure`-Klasse und ihre Unterklassen so erweitert, dass sie Iteration unterstützen. Iteration ist ein leistungsstarkes Konzept in Python, das es Ihnen ermöglicht, schrittweise durch eine Sammlung von Elementen zu iterieren. Wenn eine Klasse Iteration unterstützt, wird sie flexibler und kann mit vielen integrierten Python-Funktionen zusammenarbeiten. Lassen Sie uns untersuchen, wie diese Unterstützung für Iteration viele leistungsstarke Funktionen in Python ermöglicht.

## Nutzen von Iteration für Sequenzkonvertierungen

In Python gibt es integrierte Funktionen wie `list()` und `tuple()`. Diese Funktionen sind sehr nützlich, da sie jedes iterierbare Objekt als Eingabe akzeptieren können. Ein iterierbares Objekt ist etwas, über das Sie in einer Schleife iterieren können, wie eine Liste, ein Tupel oder jetzt auch Instanzen unserer `Structure`-Klasse. Da unsere `Structure`-Klasse jetzt Iteration unterstützt, können wir Instanzen dieser Klasse problemlos in Listen oder Tupel umwandeln.

1. Versuchen wir diese Operationen mit einer `Stock`-Instanz. Die `Stock`-Klasse ist eine Unterklasse von `Structure`. Führen Sie den folgenden Befehl in Ihrem Terminal aus:

```bash
python3 -c "from stock import Stock; s = Stock('GOOG', 100, 490.1); print('As list:', list(s)); print('As tuple:', tuple(s))"
```

Dieser Befehl importiert zunächst die `Stock`-Klasse, erstellt eine Instanz davon und wandelt diese Instanz dann mithilfe der `list()`- und `tuple()`-Funktionen in eine Liste und ein Tupel um. Die Ausgabe zeigt Ihnen die Instanz als Liste und als Tupel:

```
As list: ['GOOG', 100, 490.1]
As tuple: ('GOOG', 100, 490.1)
```

## Entpacken (Unpacking)

Python hat eine sehr nützliche Funktion namens Entpacken (Unpacking). Entpacken ermöglicht es Ihnen, ein iterierbares Objekt zu nehmen und seine Elemente auf einmal einzelnen Variablen zuzuweisen. Da unsere `Stock`-Instanz iterierbar ist, können wir diese Entpackungsfunktion darauf anwenden.

```bash
python3 -c "from stock import Stock; s = Stock('GOOG', 100, 490.1); name, shares, price = s; print(f'Name: {name}, Shares: {shares}, Price: {price}')"
```

In diesem Code erstellen wir eine `Stock`-Instanz und entpacken dann ihre Elemente in drei Variablen: `name`, `shares` und `price`. Anschließend geben wir diese Variablen aus. Die Ausgabe zeigt die Werte dieser Variablen:

```
Name: GOOG, Shares: 100, Price: 490.1
```

## Hinzufügen von Vergleichsfähigkeiten

Wenn eine Klasse Iteration unterstützt, wird es einfacher, Vergleichsoperationen zu implementieren. Vergleichsoperationen werden verwendet, um zu prüfen, ob zwei Objekte gleich sind oder nicht. Fügen wir unserer `Structure`-Klasse eine `__eq__()`-Methode hinzu, um Instanzen zu vergleichen.

1. Öffnen Sie die Datei `structure.py` erneut. Die `__eq__()`-Methode ist eine spezielle Methode in Python, die aufgerufen wird, wenn Sie den `==`-Operator verwenden, um zwei Objekte zu vergleichen. Fügen Sie den folgenden Code in die `Structure`-Klasse in der Datei `structure.py` ein:

```python
def __eq__(self, other):
    return isinstance(other, type(self)) and tuple(self) == tuple(other)
```

Diese Methode prüft zunächst, ob das `other`-Objekt eine Instanz derselben Klasse wie `self` ist, indem sie die `isinstance()`-Funktion verwendet. Dann werden sowohl `self` als auch `other` in Tupel umgewandelt und geprüft, ob diese Tupel gleich sind.

Die vollständige `structure.py`-Datei sollte jetzt wie folgt aussehen:

```python
class StructureMeta(type):
    def __new__(cls, name, bases, clsdict):
        fields = clsdict.get('_fields', [])
        for name in fields:
            clsdict[name] = property(lambda self, name=name: getattr(self, '_'+name))
        return super().__new__(cls, name, bases, clsdict)

class Structure(metaclass=StructureMeta):
    _fields = []
    def __init__(self, *args):
        if len(args) != len(self._fields):
            raise TypeError(f'Expected {len(self._fields)} arguments')
        for name, val in zip(self._fields, args):
            setattr(self, '_'+name, val)

    def __iter__(self):
        for name in self._fields:
            yield getattr(self, name)

    def __eq__(self, other):
        return isinstance(other, type(self)) and tuple(self) == tuple(other)
```

2. Nachdem Sie die `__eq__()`-Methode hinzugefügt haben, speichern Sie die Datei `structure.py`.

3. Testen wir die Vergleichsfähigkeit. Führen Sie den folgenden Befehl in Ihrem Terminal aus:

```bash
python3 -c "from stock import Stock; a = Stock('GOOG', 100, 490.1); b = Stock('GOOG', 100, 490.1); c = Stock('AAPL', 200, 123.4); print(f'a == b: {a == b}'); print(f'a == c: {a == c}')"
```

Dieser Code erstellt drei `Stock`-Instanzen: `a`, `b` und `c`. Dann vergleicht er `a` mit `b` und `a` mit `c` mithilfe des `==`-Operators. Die Ausgabe zeigt die Ergebnisse dieser Vergleiche:

```
a == b: True
a == c: False
```

4. Um sicherzustellen, dass alles korrekt funktioniert, müssen wir die Unittests ausführen. Unittests sind eine Reihe von Code, die prüfen, ob verschiedene Teile Ihres Programms wie erwartet funktionieren. Führen Sie den folgenden Befehl in Ihrem Terminal aus:

```bash
python3 teststock.py
```

Wenn alles korrekt funktioniert, sollten Sie eine Ausgabe sehen, die anzeigt, dass die Tests bestanden wurden:

```
..
----------------------------------------------------------------------
Ran 2 tests in 0.001s

OK
```

Indem wir nur zwei einfache Methoden (`__iter__()` und `__eq__()`) hinzugefügt haben, haben wir unsere `Structure`-Klasse erheblich verbessert und sie so gemacht, dass sie mehr Python-typisch und einfacher zu verwenden ist.
