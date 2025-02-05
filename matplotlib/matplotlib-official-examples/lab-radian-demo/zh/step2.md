# 创建数据

创建一个从 0 到 15（步长为 0.01）的数值数组，并使用 basic_units 包中的 radians 函数将它们转换为弧度。

```python
from basic_units import radians
x = [val*radians for val in np.arange(0, 15, 0.01)]
```
