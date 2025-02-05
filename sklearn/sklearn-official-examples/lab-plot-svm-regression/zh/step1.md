# 生成样本数据

首先，我们生成一个由40个介于0到5之间的随机值组成的样本数据集。然后，我们计算每个值的正弦函数，并每隔5个值添加一些噪声。

```python
import numpy as np

# 生成样本数据
X = np.sort(5 * np.random.rand(40, 1), axis=0)
y = np.sin(X).ravel()

# 给目标值添加噪声
y[::5] += 3 * (0.5 - np.random.rand(8))
```
