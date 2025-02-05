# 加载并准备数据

首先，我们将使用 Scikit-learn 库加载鸢尾花数据集。鸢尾花数据集包含 3 类鸢尾植物，我们将通过删除一个类别来对数据集进行二值化处理，以创建一个二分类问题。我们还将添加噪声特征，使问题更具挑战性。

```python
import numpy as np
from sklearn.datasets import load_iris

iris = load_iris()
target_names = iris.target_names
X, y = iris.data, iris.target
X, y = X[y!= 2], y[y!= 2]
n_samples, n_features = X.shape

# add noisy features
random_state = np.random.RandomState(0)
X = np.concatenate([X, random_state.randn(n_samples, 200 * n_features)], axis=1)
```
