# 生成样本数据

我们将生成一个数据集，该数据集由一个正弦目标函数和每隔五个数据点添加的强噪声组成。

```python
import numpy as np

# 生成样本数据
rng = np.random.RandomState(42)
X = 5 * rng.rand(10000, 1)
y = np.sin(X).ravel()

# 给目标添加噪声
y[::5] += 3 * (0.5 - rng.rand(X.shape[0] // 5))

X_plot = np.linspace(0, 5, 100000)[:, None]
```
