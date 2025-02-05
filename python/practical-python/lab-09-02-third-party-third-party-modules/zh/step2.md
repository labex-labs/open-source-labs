# 标准库模块

Python 标准库中的模块通常来自诸如 `/usr/local/lib/python3.6` 这样的位置。你可以通过一个简短的测试来确定：

```python
>>> import re
>>> re
<module're' from '/usr/local/lib/python3.6/re.py'>
>>>
```

在交互式解释器（REPL）中简单查看一个模块是一个很好的调试技巧。它会告诉你文件的位置。
