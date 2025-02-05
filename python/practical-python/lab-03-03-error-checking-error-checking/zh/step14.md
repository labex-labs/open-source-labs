# 练习3.8：引发异常

你在上一节中编写的 `parse_csv()` 函数允许用户选择指定的列，但这仅在输入数据文件有列标题时才有效。

修改代码，以便在同时传入 `select` 和 `has_headers=False` 参数时引发异常。例如：

```python
>>> parse_csv('/home/labex/project/prices.csv', select=['name','price'], has_headers=False)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "fileparse.py", line 9, in parse_csv
    raise RuntimeError("select argument requires column headers")
RuntimeError: select argument requires column headers
>>>
```

添加了这个检查之后，你可能会问是否应该在函数中执行其他类型的合理性检查。例如，是否应该检查文件名是否为字符串，`types` 是否为列表，或者诸如此类的事情？

一般来说，通常最好跳过此类测试，让程序在输入错误时失败。回溯消息会指出问题的根源，有助于调试。

添加上述检查的主要原因是避免代码在无意义的模式下运行（例如，使用需要列标题的功能，但同时指定没有标题）。

这表明调用代码存在编程错误。检查“不应该发生”的情况通常是个好主意。
