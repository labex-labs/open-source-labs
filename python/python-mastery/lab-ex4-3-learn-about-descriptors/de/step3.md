# Von Validatoren zu Deskriptoren

Im vorherigen Übungsaufgabe haben Sie eine Reihe von Klassen geschrieben, die Überprüfungen durchführen konnten. Beispielsweise:

```python
>>> PositiveInteger.check(10)
10
>>> PositiveInteger.check('10')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    raise TypeError('Expected %s' % cls.expected_type)
TypeError: erwartet <class 'int'>
>>> PositiveInteger.check(-10)
```

Sie können dies zu Deskriptoren erweitern, indem Sie eine einfache Änderung an der `Validator`-Basis-Klasse vornehmen. Ändern Sie sie wie folgt:

```python
# validate.py

class Validator:
    def __init__(self, name):
        self.name = name

    @classmethod
    def check(cls, value):
        return value

    def __set__(self, instance, value):
        instance.__dict__[self.name] = self.check(value)
```

Hinweis: Das Fehlen der `__get__()`-Methode im Deskriptor bedeutet, dass Python seine Standard-Implementierung der Attributsuche verwenden wird. Dies erfordert, dass der angegebene Name mit dem Namen übereinstimmt, der im Instanzwörterbuch verwendet wird.

Keine weiteren Änderungen sollten erforderlich sein. Versuchen Sie nun, die `Stock`-Klasse zu ändern, um die Validatoren als Deskriptoren zu verwenden, wie folgt:

```python
class Stock:
    name   = String('name')
    shares = PositiveInteger('shares')
    price  = PositiveFloat('price')

    def __init__(self,name,shares,price):
        self.name = name
        self.shares = shares
        self.price = price
```

Sie werden feststellen, dass Ihre Klasse auf die gleiche Weise funktioniert wie zuvor, viel weniger Code umfasst und Ihnen alle gewünschten Überprüfungen liefert:

```python
>>> s = Stock('GOOG', 100, 490.10)
>>> s.name
'GOOG'
>>> s.shares
100
>>> s.shares = 75
>>> s.shares = '75'
... TypeError...
>>> s.shares = -50
... ValueError...
>>>
```

Dies ist ziemlich cool. Deskriptoren haben es Ihnen ermöglicht, die Implementierung der `Stock`-Klasse erheblich zu vereinfachen. Dies ist die wahre Macht von Deskriptoren - Sie erhalten eine niedrige Ebene der Kontrolle über den Punkt und können damit erstaunliche Dinge tun.
