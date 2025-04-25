# 加载数据集

我们将从 scikit-learn 中加载数字数据集，并选择数据的一个子集用于数字 1 和 2 的二分类。

```python
from sklearn.datasets import load_digits

X, y = load_digits(return_X_y=True)
subset_mask = np.isin(y, [1, 2])  # 二分类：1 对 2
X, y = X[subset_mask], y[subset_mask]
```
