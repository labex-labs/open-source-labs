# 计算套索路径

接下来，我们使用 LARS 算法计算套索路径。Scikit-Learn 的 `linear_model` 模块中的 `lars_path` 函数用于计算套索路径。该函数将输入特征、目标变量和方法作为参数。在这种情况下，我们使用 “lasso” 方法进行 L1 正则化。

```python
from sklearn import linear_model

_, _, coefs = linear_model.lars_path(X, y, method="lasso", verbose=True)
```
