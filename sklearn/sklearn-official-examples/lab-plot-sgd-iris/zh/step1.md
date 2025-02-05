# 加载并准备数据

我们首先导入必要的库并加载鸢尾花数据集。然后，我们将对数据进行洗牌（打乱顺序）并标准化，以便用于训练。

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.linear_model import SGDClassifier

# 加载鸢尾花数据集
iris = datasets.load_iris()

# 取前两个特征
X = iris.data[:, :2]
y = iris.target
colors = "bry"

# 打乱数据
idx = np.arange(X.shape[0])
np.random.seed(13)
np.random.shuffle(idx)
X = X[idx]
y = y[idx]

# 标准化数据
mean = X.mean(axis=0)
std = X.std(axis=0)
X = (X - mean) / std
```
