# Übung 5.8: Hinzufügen von Slots

Ändern Sie die `Stock`-Klasse so, dass sie ein `__slots__`-Attribut hat. Anschließend überprüfen Sie, dass neue Attribute nicht hinzugefügt werden können:

```python
>>> ================================ RESTART ================================
>>> from stock import Stock
>>> s = Stock('GOOG', 100, 490.10)
>>> s.name
'GOOG'
>>> s.blah = 42
... sehen Sie, was passiert...
>>>
```

Wenn Sie `__slots__` verwenden, verwendet Python eine effizientere interne Darstellung von Objekten. Was passiert, wenn Sie versuchen, das zugrunde liegende Wörterbuch von `s` wie oben zu untersuchen?

```python
>>> s.__dict__
... sehen Sie, was passiert...
>>>
```

Es sollte bemerkt werden, dass `__slots__` am häufigsten als Optimierung für Klassen verwendet wird, die als Datenstrukturen dienen. Das Verwenden von Slots wird solche Programme dazu bringen, viel weniger Speicher zu verwenden und etwas schneller zu laufen. Auf den meisten anderen Klassen sollten Sie jedoch möglicherweise `__slots__` vermeiden.
