# 生成随机数据

在这一步中，我们将为散点图生成随机数据。我们将使用 NumPy 库为每个变量生成 50 个数据点。

```python
np.random.seed(19680801)

N = 50
x = np.random.rand(N)
y = np.random.rand(N)
```
