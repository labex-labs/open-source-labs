# C 风格格式化

你也可以使用格式化运算符 `%`。

```python
>>> 'The value is %d' % 3
'The value is 3'
>>> '%5d %-5d %10d' % (3,4,5)
'    3 4              5'
>>> '%0.2f' % (3.1415926,)
'3.14'
```

这要求右边是单个项或一个元组。格式代码也是仿照 C 语言的 `printf()`。

**注意**：这是字节串上唯一可用的格式化方式。

```python
>>> b'%s has %d messages' % (b'Dave', 37)
b'Dave has 37 messages'
>>> b'%b has %d messages' % (b'Dave', 37)  # 可以使用 %b 代替 %s
b'Dave has 37 messages'
>>>
```
