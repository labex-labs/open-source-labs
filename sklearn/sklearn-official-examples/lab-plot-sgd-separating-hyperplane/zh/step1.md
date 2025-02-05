# 导入必要的库并生成数据

首先，我们需要导入必要的库，并生成一个适合分类的数据集。在这个例子中，我们将使用Scikit-learn中的`make_blobs`函数生成50个可分离的点。

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import SGDClassifier
from sklearn.datasets import make_blobs

# 我们创建50个可分离的点
X, Y = make_blobs(n_samples=50, centers=2, random_state=0, cluster_std=0.60)
```
