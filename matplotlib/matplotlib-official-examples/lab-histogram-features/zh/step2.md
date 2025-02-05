# 生成样本数据

在这一步中，我们将使用 numpy 生成样本数据。我们将从均值为 100、标准差为 15 的正态分布中生成随机数据。

```python
np.random.seed(19680801)
mu = 100  # 分布的均值
sigma = 15  # 分布的标准差
x = mu + sigma * np.random.randn(437)
```
