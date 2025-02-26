# Übung 5.7: Eigenschaften und Setter

Ändern Sie das `shares`-Attribut so, dass der Wert in einem privaten Attribut gespeichert wird und dass eine Paar von Eigenschaftsfunktionen verwendet wird, um sicherzustellen, dass er immer als ganzzahliger Wert festgelegt wird. Hier ist ein Beispiel für das erwartete Verhalten:

```python
>>> ================================ RESTART ================================
>>> from stock import Stock
>>> s = Stock('GOOG',100,490.10)
>>> s.shares = 50
>>> s.shares = 'a lot'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: erwartet eine Ganzzahl
>>>
```
