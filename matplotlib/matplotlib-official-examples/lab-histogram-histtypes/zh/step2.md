# 生成随机数据

我们将使用NumPy的 `random.normal` 函数生成两组随机数据。这两组数据将用于创建不同样式的直方图。

```python
np.random.seed(19680801)

mu_x = 200
sigma_x = 25
x = np.random.normal(mu_x, sigma_x, size=100)

mu_w = 200
sigma_w = 10
w = np.random.normal(mu_w, sigma_w, size=100)
```
