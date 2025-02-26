# Übung 6.13: Generatorausdrücke

Generatorausdrücke sind eine Generator-Version einer List Comprehension. Beispielsweise:

```python
>>> nums = [1, 2, 3, 4, 5]
>>> squares = (x*x for x in nums)
>>> squares
<generator object <genexpr> at 0x109207e60>
>>> for n in squares:
...     print(n)
...
1
4
9
16
25
```

Im Gegensatz zu einer List Comprehension kann ein Generatorausdruck nur einmal verwendet werden. Wenn Sie daher einen weiteren for-Schleifenversuch machen, erhalten Sie nichts:

```python
>>> for n in squares:
...     print(n)
...
>>>
```
