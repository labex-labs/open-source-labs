# Einführung

Klassen können spezielle Methoden definieren. Diese haben eine besondere Bedeutung für den Python-Interpreter. Sie werden immer von `__` vor und nachgestellt. Beispielsweise `__init__`.

```python
class Stock(object):
    def __init__(self):
     ...
    def __repr__(self):
     ...
```

Es gibt Dutzende von speziellen Methoden, aber wir werden uns nur einige spezifische Beispiele ansehen.
