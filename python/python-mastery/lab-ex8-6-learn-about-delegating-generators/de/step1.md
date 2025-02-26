# Beispiel: Nachrichten empfangen

In Übung 8.3 haben wir uns die Definitionen von Coroutinen angeschaut. Coroutinen waren Funktionen, an die Sie Daten sendeten. Beispielsweise:

```python
>>> from cofollow import consumer
>>> @consumer
    def printer():
        while True:
            item = yield
            print('Got:', item)

>>> p = printer()
>>> p.send('Hello')
Got: Hello
>>> p.send('World')
Got: World
>>>
```

Damals wäre es vielleicht interessant gewesen, `yield` zum Empfang eines Werts zu verwenden. Wenn man aber den Code wirklich betrachtet, sieht er ziemlich seltsam aus - ein bloßes `yield` wie das? Was ist da los?

Definieren Sie in der Datei `cofollow.py` die folgende Funktion:

```python
def receive(expected_type):
    msg = yield
    assert isinstance(msg, expected_type), 'Expected type %s' % (expected_type)
    return msg
```

Diese Funktion empfängt eine Nachricht, überprüft jedoch, dass sie vom erwarteten Typ ist. Testen Sie es:

```python
>>> from cofollow import consumer, receive
>>> @consumer
    def print_ints():
        while True:
             val = yield from receive(int)
             print('Got:', val)

>>> p = print_ints()
>>> p.send(42)
Got: 42
>>> p.send(13)
Got: 13
>>> p.send('13')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
...
AssertionError: Expected type <class 'int'>
>>>
```

Aus Sicht der Lesbarkeit ist der Ausdruck `yield from receive(int)` etwas beschreibender - er zeigt an, dass die Funktion so lange pausiert, bis sie eine Nachricht vom angegebenen Typ erhält.

Ändern Sie nun alle Coroutinen in `coticker.py`, um die neue `receive()`-Funktion zu verwenden, und stellen Sie sicher, dass der Code aus Übung 8.3 weiterhin funktioniert.
