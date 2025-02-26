# Closures als Datenstruktur

Ein potenzieller Gebrauch von Closures ist als Werkzeug für die Datenkapselung. Probieren Sie dieses Beispiel aus:

```python
def counter(value):
    def incr():
        nonlocal value
        value += 1
        return value

    def decr():
        nonlocal value
        value -= 1
        return value

    return incr, decr
```

Dieser Code definiert zwei innere Funktionen, die einen Wert manipulieren. Testen Sie es:

```python
>>> up, down = counter(0)
>>> up()
1
>>> up()
2
>>> up()
3
>>> down()
2
>>> down()
1
>>>
```

Bemerken Sie, dass hier keine Klassendefinition beteiligt ist. Darüber hinaus gibt es auch keine globale Variable. Dennoch manipulieren die `up()`- und `down()`-Funktionen einen "im Hintergrund" liegenden Wert. Es ist ziemlich magisch.
