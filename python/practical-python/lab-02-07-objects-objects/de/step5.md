# Identität und Referenzen

Verwenden Sie den `is`-Operator, um zu überprüfen, ob zwei Werte genau dasselbe Objekt sind.

```python
>>> a = [1,2,3]
>>> b = a
>>> a is b
True
>>>
```

`is` vergleicht die Objektidentität (eine Ganzzahl). Die Identität kann mit `id()` abgerufen werden.

```python
>>> id(a)
3588944
>>> id(b)
3588944
>>>
```

Hinweis: Es ist fast immer besser, `==` zum Überprüfen von Objekten zu verwenden. Verhalten von `is` ist oft unerwartet:

```python
>>> a = [1,2,3]
>>> b = a
>>> c = [1,2,3]
>>> a is b
True
>>> a is c
False
>>> a == c
True
>>>
```
