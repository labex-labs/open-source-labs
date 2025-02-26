# Method Resolution Order oder MRO

Python berechnet eine Vererbungsfolge im Voraus und speichert sie im _MRO_-Attribut der Klasse. Sie können es anzeigen.

```python
>>> E.__mro__
(<class '__main__.E'>, <class '__main__.D'>,
 <class '__main__.B'>, <class '__main__.A'>,
 <type 'object'>)
>>>
```

Diese Folge wird als **Method Resolution Order** bezeichnet. Um ein Attribut zu finden, läuft Python die MRO in der angegebenen Reihenfolge ab. Die erste Übereinstimmung gewinnt.
