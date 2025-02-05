# 创建网格

接下来，我们将创建一个点的网格，在其上显示向量场。在本示例中，我们将使用 NumPy 的 `meshgrid` 函数创建点的网格。`arange` 函数用于在指定区间内创建等间距点的数组。

```python
x, y, z = np.meshgrid(np.arange(-0.8, 1, 0.2),
                      np.arange(-0.8, 1, 0.2),
                      np.arange(-0.8, 1, 0.8))
```
