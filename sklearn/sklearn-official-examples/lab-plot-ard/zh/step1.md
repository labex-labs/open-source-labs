# 生成合成数据集

我们生成一个合成数据集，其中 `X` 和 `y` 呈线性关联。`X` 的十个特征将用于生成 `y`。其他特征对预测 `y` 没有帮助。此外，我们生成一个 `n_samples == n_features` 的数据集。这样的设置对 OLS 模型来说具有挑战性，可能会导致权重任意大。对权重施加先验和惩罚可以缓解这个问题。最后，添加高斯噪声。

```python
from sklearn.datasets import make_regression

X, y, true_weights = make_regression(
    n_samples=100,
    n_features=100,
    n_informative=10,
    noise=8,
    coef=True,
    random_state=42,
)
```
