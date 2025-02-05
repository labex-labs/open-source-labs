# 加载并准备数据集

我们加载数字数据集，并通过提取数据和目标标签来为聚类做准备。我们还将随机种子设为零以确保可重复性。

```python
digits = datasets.load_digits()
X, y = digits.data, digits.target
n_samples, n_features = X.shape
np.random.seed(0)
```
