# 从模块中导入

这会从模块中挑选出选定的符号，并使它们在本地可用。

```python
from math import sin, cos

def rectangular(r, theta):
    x = r * cos(theta)
    y = r * sin(theta)
    return x, y
```

这样可以在不输入模块前缀的情况下使用模块的部分内容。这对于常用名称很有用。
