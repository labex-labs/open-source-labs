# Übung 2.19: Listenverständnisse

Probieren Sie ein paar einfache Listenverständnisse, um sich nur mit der Syntax vertraut zu machen.

```python
>>> nums = [1,2,3,4]
>>> squares = [ x * x for x in nums ]
>>> squares
[1, 4, 9, 16]
>>> twice = [ 2 * x for x in nums if x > 2 ]
>>> twice
[6, 8]
>>>
```

Bemerken Sie, wie die Listenverständnisse eine neue Liste mit den Daten erzeugen, die geeignet transformiert oder gefiltert sind.
