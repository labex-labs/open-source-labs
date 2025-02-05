# 加载数据集并生成随机特征

我们将使用鸢尾花数据集，该数据集包含从3种鸢尾花中获取的测量数据，并生成一些与鸢尾花数据集中的类别标签不相关的随机特征数据（即20个特征）。

```python
from sklearn.datasets import load_iris
import numpy as np

iris = load_iris()
X = iris.data
y = iris.target

n_uncorrelated_features = 20
rng = np.random.RandomState(seed=0)
X_rand = rng.normal(size=(X.shape[0], n_uncorrelated_features))
```
