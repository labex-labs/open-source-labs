# 生成随机数据

我们将使用 NumPy 为散点图生成随机数据。我们将创建 150 个具有随机半径和角度值的数据点，并计算每个点的面积和颜色。

```python
N = 150
r = 2 * np.random.rand(N)
theta = 2 * np.pi * np.random.rand(N)
area = 200 * r**2
colors = theta
```
