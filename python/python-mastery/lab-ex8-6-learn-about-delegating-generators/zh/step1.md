# 示例：接收消息

在练习8.3中，我们研究了协程的定义。协程是你向其发送数据的函数。例如：

```python
>>> from cofollow import consumer
>>> @consumer
    def printer():
        while True:
            item = yield
            print('收到：', item)

>>> p = printer()
>>> p.send('你好')
收到：你好
>>> p.send('世界')
收到：世界
>>>
```

当时，使用 `yield` 来接收值可能会很有趣。然而，如果你仔细查看代码，会发现它看起来相当奇怪——那样一个光秃秃的 `yield`？这是怎么回事呢？

在 `cofollow.py` 文件中，定义以下函数：

```python
def receive(expected_type):
    msg = yield
    assert isinstance(msg, expected_type), '期望的类型是 %s' % (expected_type)
    return msg
```

这个函数接收一条消息，然后验证它是否是期望的类型。试试看：

```python
>>> from cofollow import consumer, receive
>>> @consumer
    def print_ints():
        while True:
             val = yield from receive(int)
             print('收到：', val)

>>> p = print_ints()
>>> p.send(42)
收到：42
>>> p.send(13)
收到：13
>>> p.send('13')
回溯（最近一次调用）：
  文件 "<stdin>"，第1行，在 <模块> 中
 ...
断言错误：期望的类型是 <class 'int'>
>>>
```

从可读性的角度来看，`yield from receive(int)` 语句更具描述性——它表明该函数将暂停，直到收到给定类型的消息。

现在，修改 `coticker.py` 中的所有协程，以使用新的 `receive()` 函数，并确保练习8.3中的代码仍然有效。
