# 创建数据

在这一步中，你需要使用 `multivariate_normal()` 创建数据。此函数从多元正态分布中生成一个随机样本。

```python
data = np.vstack([
    multivariate_normal([10, 10], [[3, 2], [2, 3]], size=100000),
    multivariate_normal([30, 20], [[3, 1], [1, 3]], size=1000)
])
```
