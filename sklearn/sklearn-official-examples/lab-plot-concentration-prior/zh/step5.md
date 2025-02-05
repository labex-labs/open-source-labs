# 生成数据

在这一步中，我们使用 `numpy.random.RandomState` 函数和第三步中定义的参数来生成数据。

```python
rng = np.random.RandomState(random_state)
X = np.vstack(
    [
        rng.multivariate_normal(means[j], covars[j], samples[j])
        for j in range(n_components)
    ]
)
y = np.concatenate([np.full(samples[j], j, dtype=int) for j in range(n_components)])
```
