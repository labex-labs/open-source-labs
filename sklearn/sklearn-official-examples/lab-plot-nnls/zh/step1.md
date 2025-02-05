# 生成随机数据

我们将生成一些随机数据来测试我们的算法。我们将创建 200 个样本，每个样本有 50 个特征，并为每个特征使用 3 的真实系数。然后，我们将对系数进行阈值处理，使其为非负。最后，我们将向样本中添加一些噪声。

```python
import numpy as np

np.random.seed(42)

n_samples, n_features = 200, 50
X = np.random.randn(n_samples, n_features)
true_coef = 3 * np.random.randn(n_features)
true_coef[true_coef < 0] = 0
y = np.dot(X, true_coef)
y += 5 * np.random.normal(size=(n_samples,))
```
