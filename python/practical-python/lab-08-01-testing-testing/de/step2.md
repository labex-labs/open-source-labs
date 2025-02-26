# Vertragsprogrammierung

Auch als Design By Contract bekannt, ist das weit verbreitete Verwenden von Assertionen ein Ansatz zur Softwareentwicklung. Es besagt, dass Softwareentwickler präzise Schnittstellenbeschreibungen für die Komponenten der Software definieren sollten.

Beispielsweise könnten Sie Assertionen für alle Eingaben einer Funktion setzen.

```python
def add(x, y):
    assert isinstance(x, int), 'Expected int'
    assert isinstance(y, int), 'Expected int'
    return x + y
```

Das Überprüfen der Eingaben wird sofort aufrufende Funktionen erkennen, die nicht passende Argumente verwenden.

```python
>>> add(2, 3)
5
>>> add('2', '3')
Traceback (most recent call last):
...
AssertionError: Expected int
>>>
```
