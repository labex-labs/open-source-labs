# 作为数据结构的闭包

闭包的一个潜在用途是作为数据封装的工具。试试这个例子：

```python
def counter(value):
    def incr():
        nonlocal value
        value += 1
        return value

    def decr():
        nonlocal value
        value -= 1
        return value

    return incr, decr
```

这段代码定义了两个内部函数来操作一个值。试试看：

```python
>>> up, down = counter(0)
>>> up()
1
>>> up()
2
>>> up()
3
>>> down()
2
>>> down()
1
>>>
```

注意这里没有涉及类定义。此外，也没有全局变量。然而，`up()` 和 `down()` 函数却在操作某个“幕后”的值。这相当神奇。
