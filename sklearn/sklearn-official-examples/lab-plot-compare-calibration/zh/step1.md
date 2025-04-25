# 导入库并生成数据集

我们首先导入必要的库，并生成一个具有 100,000 个样本和 20 个特征的合成二元分类数据集。在这 20 个特征中，只有 2 个是信息性的，2 个是冗余的，其余 16 个是无信息的。在 100,000 个样本中，100 个将用于模型拟合，其余的用于测试。

```python
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split

# Generate dataset
X, y = make_classification(
    n_samples=100_000, n_features=20, n_informative=2, n_redundant=2, random_state=42
)

train_samples = 100  # Samples used for training the models
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    shuffle=False,
    test_size=100_000 - train_samples,
)
```
