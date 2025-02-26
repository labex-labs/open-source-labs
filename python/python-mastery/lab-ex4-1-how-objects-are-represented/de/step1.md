# Vorbereitung

Stellen Sie diese Laborklasse zurück, indem Sie eine einfache Version der `Stock`-Klasse verwenden, die Sie zuvor erstellt haben. Geben Sie am interaktiven Prompt eine neue Klasse namens `SimpleStock` wie folgt ein:

```python
>>> class SimpleStock:
        def __init__(self, name, shares, price):
            self.name = name
            self.shares = shares
            self.price = price
        def cost(self):
            return self.shares * self.price

>>>
```

Sobald Sie diese Klasse definiert haben, erstellen Sie einige Instanzen.

```python
>>> goog = SimpleStock('GOOG',100,490.10)
>>> ibm  = SimpleStock('IBM',50, 91.23)
>>>
```
