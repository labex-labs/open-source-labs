# Namenskorrektur

Eines der nervigen Dinge bei Deskriptoren ist die redundanten Namensangaben. Beispielsweise:

```python
class Stock:
 ...
    shares = PositiveInteger('shares')
 ...
```

Wir können das beheben. Ändern Sie die oberste `Validator`-Klasse, um eine `__set_name__()`-Methode wie folgt hinzuzufügen:

```python
# validate.py

class Validator:
    def __init__(self, name=None):
        self.name = name

    def __set_name__(self, cls, name):
        self.name = name

    @classmethod
    def check(cls, value):
        return value

    def __set__(self, instance, value):
        instance.__dict__[self.name] = self.check(value)
```

Versuchen Sie nun, Ihre `Stock`-Klasse so umzuschreiben, dass sie wie folgt aussieht:

```python
class Stock:
    name   = String()
    shares = PositiveInteger()
    price  = PositiveFloat()

    def __init__(self,name,shares,price):
        self.name = name
        self.shares = shares
        self.price = price
```

Ah, viel schöner. Beachten Sie jedoch, dass diese Möglichkeit, den Namen zu setzen, ein Feature von Python 3.6 ist. Es wird nicht auf älteren Versionen funktionieren.
