# 加载数据集

在这一步中，我们将从 scikit-learn 库中加载糖尿病数据集并对数据进行标准化。

```python
from sklearn import datasets

# 加载糖尿病数据集
X, y = datasets.load_diabetes(return_X_y=True)

# 标准化数据
X /= X.std(axis=0)
```
