# 创建用于可视化的数据

接下来，我们将创建一个用于可视化的二维网格。我们可以使用 NumPy 中的 `meshgrid` 函数来创建网格。`meshgrid` 函数根据两个向量 `x` 和 `y` 创建一个点的网格，这两个向量表示网格点的坐标。我们将使用以下代码块创建一个 5x5 点的网格：

```python
nrows = 5
ncols = 5
x = np.arange(ncols + 1)
y = np.arange(nrows + 1)
X, Y = np.meshgrid(x, y)
Z = X + Y
```
