# 导入必要的库和数据集

首先，我们将导入必要的库，并从 scikit-learn 中加载鸢尾花数据集。

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.gaussian_process.kernels import RBF

iris = datasets.load_iris()
X = iris.data[:, :2]  # 我们只取前两个特征。
y = np.array(iris.target, dtype=int)
```
