# Experimentieren mit exec()

Definieren Sie einen Python-Codeausschnitt in einem String und versuchen Sie, ihn auszuführen:

```python
>>> code = '''
for i in range(n):
    print(i, end=' ')
'''
>>> n = 10
>>> exec(code)
0 1 2 3 4 5 6 7 8 9
>>>
```

Das ist interessant, aber das Ausführen von zufälligen Codefragmenten ist nicht besonders nützlich. Ein interessanteres Anwendungsgebiet von `exec()` besteht darin, Code wie Funktionen, Methoden oder Klassen zu erstellen. Versuchen Sie dieses Beispiel, in dem wir eine `__init__()`-Funktion für eine Klasse erstellen.

```python
>>> class Stock:
        _fields = ('name','shares', 'price')

>>> argstr = ','.join(Stock._fields)
>>> code = f'def __init__(self, {argstr}):\n'
>>> for name in Stock._fields:
        code += f'    self.{name} = {name}\n'
>>> print(code)
def __init__(self, name,shares,price):
    self.name = name
    self.shares = shares
    self.price = price

>>> locs = { }
>>> exec(code, locs)
>>> Stock.__init__ = locs['__init__']

>>> # Jetzt testen Sie die Klasse
>>> s = Stock('GOOG', 100, 490.1)
>>> s.name
'GOOG'
>>> s.shares
100
>>> s.price
490.1
>>>
```

In diesem Beispiel wird eine `__init__()`-Funktion direkt aus der `_fields`-Variable erstellt. Es gibt keine seltsamen Tricks, die auf eine spezielle `_init()`-Methode oder Stapelrahmen Bezug nehmen.
