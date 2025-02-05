# 导入库并生成数据

首先，我们需要导入必要的库并生成一些示例数据以供使用。在这个例子中，我们将使用numpy生成数据，并使用matplotlib进行可视化。

```python
import matplotlib.pyplot as plt
import numpy as np

# 示例数据
x = np.arange(0.1, 4, 0.1)
y1 = np.exp(-1.0 * x)
y2 = np.exp(-0.5 * x)

# 示例可变误差线值
y1err = 0.1 + 0.1 * np.sqrt(x)
y2err = 0.1 + 0.1 * np.sqrt(x/2)
```
