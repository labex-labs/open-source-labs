# 生成数据

接下来，我们将生成用于创建线框绘图的数据。在本实验中，我们将使用 `np.meshgrid()` 函数来创建 X、Y 和 Z 坐标。

```python
# 生成数据
X, Y = np.meshgrid(np.arange(-5, 5, 0.25), np.arange(-5, 5, 0.25))
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)
```
