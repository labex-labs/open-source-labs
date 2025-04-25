# 生成数据

接下来，我们将使用 numpy 生成一个噪声数据集。我们将生成 20 个样本，每个样本有 2 个特征。

```python
EPSILON = np.finfo(np.float32).eps
n_samples = 20
seed = np.random.RandomState(seed=3)
X_true = seed.randint(0, 20, 2 * n_samples).astype(float)
X_true = X_true.reshape((n_samples, 2))
# 使数据居中
X_true -= X_true.mean()
```
