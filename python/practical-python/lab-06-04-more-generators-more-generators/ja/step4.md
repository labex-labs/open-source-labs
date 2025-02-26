# 演習6.13: ジェネレータ式

ジェネレータ式は、リスト内包表記のジェネレータ版です。たとえば：

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

リスト内包表記とは異なり、ジェネレータ式は一度だけ使用できます。したがって、別のforループを試すと、何も得られません：

```python
>>> for n in squares:
...     print(n)
...
>>>
```
