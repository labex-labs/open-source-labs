# 生成随机数据

首先，我们需要生成具有判别性特征和噪声特征的随机数据。我们将使用scikit-learn的`make_blobs`函数来生成具有一个判别性特征的两个数据簇。然后，我们将向其他特征添加随机噪声。

```python
import numpy as np
from sklearn.datasets import make_blobs

def generate_data(n_samples, n_features):
    """生成具有噪声特征的随机类似斑点的数据。

    这将返回一个形状为`(n_samples, n_features)`的输入数据数组
    和一个包含`n_samples`个目标标签的数组。

    只有一个特征包含判别性信息，其他特征
    只包含噪声。
    """
    X, y = make_blobs(n_samples=n_samples, n_features=1, centers=[[-2], [2]])

    # 添加非判别性特征
    if n_features > 1:
        X = np.hstack([X, np.random.randn(n_samples, n_features - 1)])
    return X, y
```
