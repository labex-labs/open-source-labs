# Private Attribute

Jeder Attributname mit führendem `_` wird als _privat_ betrachtet.

```python
class Person(object):
    def __init__(self, name):
        self._name = 0
```

Wie bereits erwähnt, ist dies nur ein Programmierstil. Sie können es immer noch zugreifen und ändern.

```python
>>> p = Person('Guido')
>>> p._name
'Guido'
>>> p._name = 'Dave'
>>>
```

Als allgemeine Regel gilt, dass jeder Name mit führendem `_` als interne Implementierung betrachtet wird, ob es sich um eine Variable, eine Funktion oder einen Modulnamen handelt. Wenn Sie sich finden, dass Sie solche Namen direkt verwenden, tun Sie wahrscheinlich etwas falsch. Suchen Sie nach höherebenen Funktionalität.
