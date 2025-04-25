# 导入必要的库并创建数据

```python
import matplotlib.pyplot as plt
import numpy as np

# 创建数据
t = np.arange(0.0, 100.0, 0.1)
s = np.sin(0.1 * np.pi * t) * np.exp(-t * 0.01)
```

首先，我们导入必要的库，即 Matplotlib 和 NumPy。然后我们创建要绘制的数据。在这个例子中，我们创建一个 numpy 数组“t”，并使用 t 计算另一个 numpy 数组“s”。
