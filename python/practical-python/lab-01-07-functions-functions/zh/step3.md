# 错误与异常

函数将错误报告为异常。异常会导致函数中止，如果未处理，可能会使整个程序停止。

在你的 Python 交互式解释器中试试这个。

```python
>>> int('N/A')
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: 'N/A'
>>>
```

出于调试目的，错误消息会描述发生了什么、错误发生在哪里，以及一个回溯信息，显示导致失败的其他函数调用。
