# 创建图表

接下来，让我们创建一个简单的图表来进行操作。我们将使用NumPy生成一些随机数据来绘制图表。

```python
import numpy as np

# 生成随机数据
np.random.seed(19680801)
data = 100 * np.random.rand(20)

# 创建图表
fig, ax = plt.subplots()
ax.plot(data)
```
