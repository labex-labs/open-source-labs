# 练习 6.13：生成器表达式

生成器表达式是列表推导式的生成器版本。例如：

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

与列表推导式不同，生成器表达式只能使用一次。因此，如果你再尝试另一个 for 循环，就不会得到任何结果：

```python
>>> for n in squares:
...     print(n)
...
>>>
```
