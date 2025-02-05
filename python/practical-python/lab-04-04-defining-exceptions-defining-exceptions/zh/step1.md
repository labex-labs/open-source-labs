# 练习4.11：定义自定义异常

对于库来说，定义自己的异常通常是个好习惯。

这样做便于区分因常见编程错误而引发的Python异常，与库为了表明特定使用问题而故意引发的异常。

修改上一个练习中的 `create_formatter()` 函数，使其在用户提供错误的格式名称时引发自定义的 `FormatError` 异常。

例如：

```python
>>> from tableformat import create_formatter
>>> formatter = create_formatter('xls')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "tableformat.py", line 80, in create_formatter
    raise FormatError(f"Unknown table format {name}")
tableformat.FormatError: Unknown table format xls
>>>
```
