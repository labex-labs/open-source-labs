# Mapping

Eine der häufigsten Operationen in der funktionalen Programmierung ist die `map()`-Operation, die eine Funktion auf die Werte in einer Sequenz abbildet. Python hat eine integrierte `map()`-Funktion, die dies tut. Beispielsweise:

```python
>>> nums = [1,2,3,4]
>>> squares = map(lambda x: x*x, nums)
>>> for n in squares:
        print(n)

1
4
9
16
>>>
```

`map()` erzeugt einen Iterator, also müssen Sie explizit eine Liste erstellen, wenn Sie eine Liste möchten:

```python
>>> squares = list(map(lambda x: x*x, nums))
>>> squares
[1, 4, 9, 16]
>>>
```

Versuchen Sie, `map()` in Ihrer `convert_csv()`-Funktion zu verwenden.
