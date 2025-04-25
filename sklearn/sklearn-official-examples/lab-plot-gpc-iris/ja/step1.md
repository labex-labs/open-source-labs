# 必要なライブラリとデータセットのインポート

まず、必要なライブラリをインポートし、scikit-learn から Iris データセットを読み込みます。

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.gaussian_process.kernels import RBF

iris = datasets.load_iris()
X = iris.data[:, :2]  # 最初の 2 つの特徴のみを取ります。
y = np.array(iris.target, dtype=int)
```
