# Durchsetzung

Ändern Sie die `ValidatedFunction`-Klasse, sodass sie die über Funktionsannotationen angehängten Wertprüfungen durchsetzt. Beispielsweise:

```python
>>> def add(x: Integer, y:Integer):
        return x + y
>>> add = ValidatedFunction(add)
>>> add(2,3)
5
>>> add('two','three')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "validate.py", line 67, in __call__
    self.func.__annotations__[name].check(val)
  File "validate.py", line 21, in check
    raise TypeError(f'Expected {cls.expected_type}')
TypeError: expected <class 'int'>
>>>>
```

Hinweis: Um dies zu tun, experimentieren Sie mit der Signaturbindung. Verwenden Sie die `bind()`-Methode von `Signature`-Objekten, um Funktionsargumente an Argumentnamen zu binden. Anschließend vergleichen Sie diese Informationen mit dem `__annotations__`-Attribut, um die verschiedenen Validator-Klassen zu erhalten.

Denken Sie daran, dass Sie ein Objekt erstellen, das wie eine Funktion aussieht, aber es tatsächlich nicht ist. Es geschieht magische Dinge im Hintergrund.
