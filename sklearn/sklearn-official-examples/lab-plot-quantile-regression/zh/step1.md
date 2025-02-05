# 数据集生成

我们将使用与单个特征 `x` 的线性关系生成两个具有相同期望值的合成数据集。我们将向数据集中添加异方差正态噪声和非对称帕累托噪声。

```python
import numpy as np

rng = np.random.RandomState(42)
x = np.linspace(start=0, stop=10, num=100)
X = x[:, np.newaxis]
y_true_mean = 10 + 0.5 * x

# 异方差正态噪声
y_normal = y_true_mean + rng.normal(loc=0, scale=0.5 + 0.5 * x, size=x.shape[0])

# 非对称帕累托噪声
a = 5
y_pareto = y_true_mean + 10 * (rng.pareto(a, size=x.shape[0]) - 1 / (a - 1))
```
