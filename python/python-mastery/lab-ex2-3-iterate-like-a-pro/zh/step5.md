# 生成器表达式

生成器表达式几乎与列表推导式完全相同，只是它不会创建列表。相反，它创建一个对象，该对象会逐步生成结果 —— 通常用于通过迭代来使用。试试这个简单的例子：

```python
>>> nums = [1,2,3,4,5]
>>> squares = (x*x for x in nums)
>>> squares
<generator object <genexpr> at 0x37caa8>
>>> for n in squares:
        print(n)

1
4
9
16
25
>>>
```

你会注意到生成器表达式只能使用一次。看看如果你再次执行 for 循环会发生什么：

```python
>>> for n in squares:
         print(n)

>>>
```

如果你使用 `next()` 函数，可以一次手动获取一个结果。试试这个：

```python
>>> squares = (x*x for x in nums)
>>> next(squares)
1
>>> next(squares)
4
>>> next(squares)
9
>>>
```

不断输入 `next()`，看看没有更多数据时会发生什么。

如果你正在执行的任务更复杂，你仍然可以通过编写生成器函数并使用 `yield` 语句来利用生成器。例如：

```python
>>> def squares(nums):
        for x in nums:
            yield x*x

>>> for n in squares(nums):
        print(n)

1
4
9
16
25
>>>
```

在本课程后面我们会再回到生成器函数 —— 目前，只需将此类函数视为具有将值提供给 `for` 语句的有趣特性即可。
