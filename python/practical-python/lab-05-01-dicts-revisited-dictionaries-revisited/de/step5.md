# Instanzen und Klassen

Instanzen und Klassen sind miteinander verknüpft. Das Attribut `__class__` verweist zurück auf die Klasse.

```python
>>> s = Stock('GOOG', 100, 490.1)
>>> s.__dict__
{ 'name': 'GOOG','shares': 100, 'price': 490.1 }
>>> s.__class__
<class '__main__.Stock'>
>>>
```

Das Instanzwörterbuch enthält Daten, die für jede Instanz einzigartig sind, während das Klassenwörterbuch Daten enthält, die von _allen_ Instanzen gemeinsam geteilt werden.
