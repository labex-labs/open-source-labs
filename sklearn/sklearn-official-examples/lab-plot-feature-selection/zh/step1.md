# 生成示例数据

首先，我们将为演示生成一些示例数据。我们将使用鸢尾花数据集，并向其中添加一些不相关的噪声数据。

```python
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

# 鸢尾花数据集
X, y = load_iris(return_X_y=True)

# 一些不相关的噪声数据
E = np.random.RandomState(42).uniform(0, 0.1, size=(X.shape[0], 20))

# 将噪声数据添加到信息特征中
X = np.hstack((X, E))

# 分割数据集以选择特征并评估分类器
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, random_state=0)
```
