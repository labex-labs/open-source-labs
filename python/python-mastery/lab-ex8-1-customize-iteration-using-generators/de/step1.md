# Ein einfacher Generator

Wenn Sie jemals feststellen, dass Sie die Iteration anpassen möchten, sollten Sie immer an Generatorfunktionen denken. Sie sind einfach zu schreiben - einfach erstellen Sie eine Funktion, die die gewünschte Iterationslogik ausführt und `yield` verwendet, um Werte auszugeben.

Beispielsweise versuchen Sie diesen Generator, mit dem Sie über einen Bereich von Zahlen mit Bruchschritten iterieren können (etwas, das von der integrierten `range()`-Funktion nicht unterstützt wird):

```python
>>> def frange(start,stop,step):
        while start < stop:
            yield start
            start += step

>>> for x in frange(0, 2, 0.25):
        print(x, end=' ')

0 0.25 0.5 0.75 1.0 1.25 1.5 1.75
>>>
```

Das Iterieren über einen Generator ist eine einmalige Operation. Beispielsweise zeigt das Folgende, was passiert, wenn Sie versuchen, zweimal zu iterieren:

```python
>>> f = frange(0, 2, 0.25)
>>> for x in f:
        print(x, end=' ')

0 0.25 0.5 0.75 1.0 1.25 1.5 1.75
>>> for x in f:
        print(x, end=' ')

>>>
```

Wenn Sie über die gleiche Sequenz iterieren möchten, müssen Sie den Generator erneut erstellen, indem Sie `frange()` erneut aufrufen. Alternativ können Sie alles in eine Klasse verpacken:

```python
>>> class FRange:
        def __init__(self, start, stop, step):
            self.start = start
            self.stop = stop
            self.step = step
        def __iter__(self):
            n = self.start
            while n < self.stop:
                yield n
                n += self.step

>>> f = FRange(0, 2, 0.25)
>>> for x in f:
        print(x, end=' ')

0 0.25 0.5 0.75 1.0 1.25 1.5 1.75
>>> for x in f:
        print(x, end=' ')

0 0.25 0.5 0.75 1.0 1.25 1.5 1.75
>>>
```
