# 生成散点图的数据

接下来，我们生成散点图的数据。我们创建 100 个数据点，其 x 和 y 值在 0 到 0.9 之间随机生成，半径在 0 到 10 之间随机生成。每个数据点的颜色由其面积的平方根决定。

```python
N = 100
r0 = 0.6
x = 0.9 * np.random.rand(N)
y = 0.9 * np.random.rand(N)
area = (20 * np.random.rand(N))**2  # 0 到 10 的点半径
c = np.sqrt(area)
```
