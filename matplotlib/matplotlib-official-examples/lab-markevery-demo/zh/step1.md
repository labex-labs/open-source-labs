# 定义数据点

首先，我们定义将用于绘图的数据点。在这个例子中，我们使用 `numpy` 生成一组正弦波的 x 和 y 值。

```python
import matplotlib.pyplot as plt
import numpy as np

# 定义要绘制的 markevery 情况列表
cases = [
    None,
    8,
    (30, 8),
    [16, 24, 32],
    [0, -1],
    slice(100, 200, 3),
    0.1,
    0.4,
    (0.2, 0.4)
]

# 数据点
delta = 0.11
x = np.linspace(0, 10 - 2 * delta, 200) + delta
y = np.sin(x) + 1.0 + delta
```
