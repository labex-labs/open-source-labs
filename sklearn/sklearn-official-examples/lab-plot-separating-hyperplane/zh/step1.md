# 创建一个两类可分离数据集

为了创建一个两类可分离数据集，我们将使用scikit-learn中的`make_blobs()`函数。此函数生成用于聚类和分类的各向同性高斯数据点集。我们将创建40个样本，有两个中心点，并设置随机种子为6。我们还将使用`matplotlib`绘制数据点。

```python
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs

# 创建一个两类可分离数据集
X, y = make_blobs(n_samples=40, centers=2, random_state=6)

# 绘制数据点
plt.scatter(X[:, 0], X[:, 1], c=y, s=30, cmap=plt.cm.Paired)
plt.show()
```
