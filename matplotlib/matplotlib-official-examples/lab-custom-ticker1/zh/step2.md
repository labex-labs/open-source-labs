# 定义自定义刻度函数

接下来，我们需要定义自定义刻度函数。自定义刻度函数接受两个参数——值和刻度位置——并返回格式化后的刻度标签。在这种情况下，我们将把刻度标签格式化为以百万美元为单位。

```python
def millions(x, pos):
    """The two arguments are the value and tick position."""
    return f'${x*1e-6:1.1f}M'
```
