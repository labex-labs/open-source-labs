# 数据

我们生成了一个包含 2000 个样本、2 个特征和 3 个目标类别的分类数据集。然后，我们按如下方式划分数据：

- 训练集：600 个样本（用于训练分类器）
- 验证集：400 个样本（用于校准预测概率）
- 测试集：1000 个样本

```python
import numpy as np
from sklearn.datasets import make_blobs

np.random.seed(0)

X, y = make_blobs(
    n_samples=2000, n_features=2, centers=3, random_state=42, cluster_std=5.0
)
X_train, y_train = X[:600], y[:600]
X_valid, y_valid = X[600:1000], y[600:1000]
X_train_valid, y_train_valid = X[:1000], y[:1000]
X_test, y_test = X[1000:], y[1000:]
```
