# 生成密集数据

接下来，我们生成一些将用于Lasso回归的密集数据。我们使用Scikit-learn的`make_regression`函数来生成具有5000个特征的200个样本。

```python
X, y = make_regression(n_samples=200, n_features=5000, random_state=0)
```
