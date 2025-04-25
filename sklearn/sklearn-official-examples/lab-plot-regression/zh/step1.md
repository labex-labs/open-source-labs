# 生成样本数据

我们首先生成用于回归问题的样本数据。我们创建一个包含 40 个数据点且只有 1 个特征的数组，然后通过对数据应用正弦函数来创建目标数组。我们还会对每第 5 个数据点添加一些噪声。

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn import neighbors

np.random.seed(0)
X = np.sort(5 * np.random.rand(40, 1), axis=0)
T = np.linspace(0, 5, 500)[:, np.newaxis]
y = np.sin(X).ravel()

# Add noise to targets
y[::5] += 1 * (0.5 - np.random.rand(8))
```
