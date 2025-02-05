# 生成数据

我们将生成一个仅包含3个信息性特征的合成数据集。我们将明确不打乱数据集，以确保信息性特征与X的前三列相对应。此外，我们将把数据集拆分为训练子集和测试子集。

```python
X, y = make_classification(
    n_samples=1000,
    n_features=10,
    n_informative=3,
    n_redundant=0,
    n_repeated=0,
    n_classes=2,
    random_state=0,
    shuffle=False,
)
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, random_state=42)
```
