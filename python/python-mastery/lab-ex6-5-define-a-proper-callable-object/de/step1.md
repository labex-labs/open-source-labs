# Vorbereitung

Im Rahmen der Übung 4.3 haben Sie eine Reihe von `Validator`-Klassen erstellt, um verschiedene Arten von Typ- und Wertprüfungen durchzuführen. Beispielsweise:

```python
>>> from validate import Integer
>>> Integer.check(1)
>>> Integer.check('hello')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "validate.py", line 21, in check
    raise TypeError(f'Expected {cls.expected_type}')
TypeError: Expected <class 'int'>
>>>
```

Sie könnten die Validatoren in Funktionen wie folgt verwenden:

```python
>>> def add(x, y):
        Integer.check(x)
        Integer.check(y)
        return x + y

>>>
```

In dieser Übung werden wir dies um einen Schritt weitergehend machen.
