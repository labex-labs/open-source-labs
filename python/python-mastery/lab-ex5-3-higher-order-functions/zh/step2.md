# 映射

函数式编程中最常见的操作之一是 `map()` 操作，它将一个函数应用于序列中的每个值。Python 有一个内置的 `map()` 函数来执行此操作。例如：

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

`map()` 返回一个迭代器，所以如果你想要一个列表，就需要显式地创建它：

```python
>>> squares = list(map(lambda x: x*x, nums))
>>> squares
[1, 4, 9, 16]
>>>
```

尝试在你的 `convert_csv()` 函数中使用 `map()`。
