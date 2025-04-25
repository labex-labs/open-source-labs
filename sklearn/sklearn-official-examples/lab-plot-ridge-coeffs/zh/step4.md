# 使用不同的正则化强度训练模型

我们将使用循环，用不同的正则化强度来训练模型。我们会通过在`set_params`函数中更改 alpha 的值来设置正则化强度。我们将保存每个 alpha 值对应的系数和误差。

```python
coefs = []
errors = []

alphas = np.logspace(-6, 6, 200)

for a in alphas:
    clf.set_params(alpha=a)
    clf.fit(X, y)
    coefs.append(clf.coef_)
    errors.append(mean_squared_error(clf.coef_, w))
```
