# 相对导入

你可以使用 `.` 来指代当前包，而不是直接使用包名。

```python
from. import fileparse

def read_portfolio(filename):
    return fileparse.parse_csv(...)
```

语法：

```python
from. import modname
```

这样便于重命名包。
