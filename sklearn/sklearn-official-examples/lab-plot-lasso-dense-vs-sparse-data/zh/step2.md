# 生成密集数据

接下来，我们生成一些将用于 Lasso 回归的密集数据。我们使用 Scikit-learn 的`make_regression`函数来生成具有 5000 个特征的 200 个样本。

```python
X, y = make_regression(n_samples=200, n_features=5000, random_state=0)
```
