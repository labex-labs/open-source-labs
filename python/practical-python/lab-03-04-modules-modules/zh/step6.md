# `import as` 语句

你可以在导入模块时更改其名称：

```python
import math as m
def rectangular(r, theta):
    x = r * m.cos(theta)
    y = r * m.sin(theta)
    return x, y
```

它的工作方式与普通导入相同。只是在该文件中重命名了模块。
