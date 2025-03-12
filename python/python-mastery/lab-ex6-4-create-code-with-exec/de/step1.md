# Grundlagen der `exec()`-Funktion verstehen

In Python ist die `exec()`-Funktion ein leistungsstarkes Werkzeug, das es Ihnen ermöglicht, Code auszuführen, der zur Laufzeit dynamisch erstellt wird. Dies bedeutet, dass Sie Code "on the fly" basierend auf bestimmten Eingaben oder Konfigurationen generieren können, was in vielen Programmier-Szenarien äußerst nützlich ist.

Beginnen wir damit, die grundlegende Verwendung der `exec()`-Funktion zu untersuchen. Dazu öffnen wir eine Python-Shell. Öffnen Sie Ihr Terminal und geben Sie `python3` ein. Dieser Befehl startet den interaktiven Python-Interpreter, in dem Sie direkt Python-Code ausführen können.

```bash
python3
```

Nun werden wir ein Stück Python-Code als Zeichenkette definieren und dann die `exec()`-Funktion verwenden, um ihn auszuführen. So funktioniert es:

```python
>>> code = '''
for i in range(n):
    print(i, end=' ')
'''
>>> n = 10
>>> exec(code)
0 1 2 3 4 5 6 7 8 9
```

In diesem Beispiel:

1. Zunächst haben wir eine Zeichenkette namens `code` definiert. Diese Zeichenkette enthält eine Python-`for`-Schleife. Die Schleife ist so konzipiert, dass sie `n` Mal durchläuft und die Nummer jeder Iteration ausgibt.
2. Dann haben wir eine Variable `n` definiert und ihr den Wert 10 zugewiesen. Diese Variable wird als obere Grenze für die `range()`-Funktion in unserer Schleife verwendet.
3. Danach haben wir die `exec()`-Funktion mit der `code`-Zeichenkette als Argument aufgerufen. Die `exec()`-Funktion nimmt die Zeichenkette und führt sie als Python-Code aus.
4. Schließlich hat die Schleife ausgeführt und die Zahlen von 0 bis 9 ausgegeben.

Die wirkliche Stärke der `exec()`-Funktion wird deutlicher, wenn wir sie verwenden, um komplexere Code-Strukturen wie Funktionen oder Methoden zu erstellen. Versuchen wir ein fortgeschritteneres Beispiel, in dem wir dynamisch eine `__init__()`-Methode für eine Klasse erstellen.

```python
>>> class Stock:
...     _fields = ('name', 'shares', 'price')
...
>>> argstr = ','.join(Stock._fields)
>>> code = f'def __init__(self, {argstr}):\n'
>>> for name in Stock._fields:
...     code += f'    self.{name} = {name}\n'
...
>>> print(code)
def __init__(self, name,shares,price):
    self.name = name
    self.shares = shares
    self.price = price

>>> locs = { }
>>> exec(code, locs)
>>> Stock.__init__ = locs['__init__']

>>> # Now try the class
>>> s = Stock('GOOG', 100, 490.1)
>>> s.name
'GOOG'
>>> s.shares
100
>>> s.price
490.1
```

In diesem komplexeren Beispiel:

1. Zunächst haben wir eine `Stock`-Klasse mit einem `_fields`-Attribut definiert. Dieses Attribut ist ein Tupel, das die Namen der Attribute der Klasse enthält.
2. Dann haben wir eine Zeichenkette erstellt, die Python-Code für eine `__init__`-Methode darstellt. Diese Methode wird verwendet, um die Attribute des Objekts zu initialisieren.
3. Als Nächstes haben wir die `exec()`-Funktion verwendet, um die Code-Zeichenkette auszuführen. Wir haben auch ein leeres Dictionary `locs` an `exec()` übergeben. Die resultierende Funktion aus der Ausführung wird in diesem Dictionary gespeichert.
4. Danach haben wir die im Dictionary gespeicherte Funktion als `__init__`-Methode unserer `Stock`-Klasse zugewiesen.
5. Schließlich haben wir eine Instanz der `Stock`-Klasse erstellt und überprüft, ob die `__init__`-Methode korrekt funktioniert, indem wir auf die Attribute des Objekts zugegriffen haben.

Dieses Beispiel zeigt, wie die `exec()`-Funktion verwendet werden kann, um Methoden dynamisch basierend auf Daten zu erstellen, die zur Laufzeit verfügbar sind.
