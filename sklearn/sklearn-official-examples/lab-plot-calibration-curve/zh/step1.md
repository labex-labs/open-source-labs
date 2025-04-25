# 数据集

我们将使用一个合成的二元分类数据集，它有 100,000 个样本和 20 个特征。在这 20 个特征中，只有 2 个是有信息的，10 个是冗余的（有信息特征的随机组合），其余 8 个是无信息的（随机数）。在这 100,000 个样本中，1,000 个将用于模型拟合，其余的用于测试。

```python
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split

X, y = make_classification(
    n_samples=100_000, n_features=20, n_informative=2, n_redundant=10, random_state=42
)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.99, random_state=42
)
```
