# 加载数据集

我们将使用 `sklearn.datasets` 中的 `make_circles` 函数创建一个由两个嵌套圆圈组成的数据集。

```python
from sklearn.datasets import make_circles
from sklearn.model_selection import train_test_split

X, y = make_circles(n_samples=1_000, factor=0.3, noise=0.05, random_state=0)
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, random_state=0)
```
