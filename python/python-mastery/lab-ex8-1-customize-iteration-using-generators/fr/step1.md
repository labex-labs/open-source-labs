# Un générateur simple

Si vous vous trouvez à avoir besoin de personnaliser l'itération, vous devriez toujours penser aux fonctions génératrices. Elles sont faciles à écrire - il suffit de créer une fonction qui exécute la logique d'itération souhaitée et utilise `yield` pour émettre des valeurs.

Par exemple, essayez ce générateur qui vous permet d'itérer sur une plage de nombres avec des pas fractionnaires (ce qui n'est pas pris en charge par la fonction intégrée `range()`):

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

L'itération sur un générateur est une opération unique. Par exemple, voici ce qui se passe si vous essayez d'itérer deux fois:

```python
>>> f = frange(0, 2, 0.25)
>>> for x in f:
        print(x, end=' ')

0 0.25 0.5 0.75 1.0 1.25 1.5 1.75
>>> for x in f:
        print(x, end=' ')

>>>
```

Si vous voulez itérer sur la même séquence, vous devez recreer le générateur en appelant `frange()` à nouveau. Alternativement, vous pourriez emballer tout dans une classe:

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
