# 设置随机种子并生成数据

在这一步中，我们将设置随机种子并生成数据。我们将从均值为 200、标准差为 25 的正态分布中生成 100 个数据点。

```python
np.random.seed(19680801)
mu = 200
sigma = 25
data = np.random.normal(mu, sigma, size=100)
```
