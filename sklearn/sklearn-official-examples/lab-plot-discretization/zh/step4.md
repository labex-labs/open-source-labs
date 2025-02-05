# 对输入特征进行离散化

在这一步中，我们将使用KBinsDiscretizer类对输入特征进行离散化。我们将创建10个区间，并使用独热编码来转换数据。

```python
enc = KBinsDiscretizer(n_bins=10, encode="onehot")
X_binned = enc.fit_transform(X)
```
