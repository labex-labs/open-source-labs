# 生成器

生成器是一种定义迭代的函数。

```python
def countdown(n):
    while n > 0:
        yield n
        n -= 1
```

例如：

```python
>>> for x in countdown(10):
...   print(x, end=' ')
...
10 9 8 7 6 5 4 3 2 1
>>>
```

生成器是任何使用 `yield` 语句的函数。

生成器的行为与普通函数不同。调用生成器函数会创建一个生成器对象。它不会立即执行函数。

```python
def countdown(n):
    # 添加了一条打印语句
    print('Counting down from', n)
    while n > 0:
        yield n
        n -= 1
```

```python
>>> x = countdown(10)
# 没有打印语句
>>> x
# x 是一个生成器对象
<generator object at 0x58490>
>>>
```

函数仅在调用 `__next__()` 时执行。

```python
>>> x = countdown(10)
>>> x
<generator object at 0x58490>
>>> x.__next__()
Counting down from 10
10
>>>
```

`yield` 产生一个值，但会暂停函数执行。函数会在下次调用 `__next__()` 时恢复执行。

```python
>>> x.__next__()
9
>>> x.__next__()
8
```

当生成器最终返回时，迭代会引发一个错误。

```python
>>> x.__next__()
1
>>> x.__next__()
Traceback (most recent call last):
File "<stdin>", line 1, in? StopIteration
>>>
```

_观察：生成器函数实现了与 for 语句在列表、元组、字典、文件等上使用的相同低级协议。_
