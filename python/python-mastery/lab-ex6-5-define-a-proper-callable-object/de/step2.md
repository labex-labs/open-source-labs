# Erstellen eines aufrufbaren Objekts

Öffnen Sie in der Datei `validate.py` und erstellen Sie eine Klasse wie folgt:

```python
# validate.py
...

class ValidatedFunction:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print('Calling', self.func)
        result = self.func(*args, **kwargs)
        return result
```

Testen Sie die Klasse, indem Sie sie auf eine Funktion anwenden:

```python
>>> def add(x, y):
        return x + y

>>> add = ValidatedFunction(add)
>>> add(2, 3)
Calling <function add at 0x1014df598>
5
>>>
```
