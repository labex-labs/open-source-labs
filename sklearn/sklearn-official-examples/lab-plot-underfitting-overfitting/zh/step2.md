# 生成数据

我们将从余弦函数生成 30 个样本，并在样本中添加一些随机噪声。

```python
def true_fun(X):
    return np.cos(1.5 * np.pi * X)

np.random.seed(0)

n_samples = 30

X = np.sort(np.random.rand(n_samples))
y = true_fun(X) + np.random.randn(n_samples) * 0.1
```
