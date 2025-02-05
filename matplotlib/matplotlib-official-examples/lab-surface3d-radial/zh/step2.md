# 创建网格

接下来，我们将在极坐标中创建网格并计算相应的 Z 值。我们将创建一个半径值数组 `r`，一个角度值数组 `p`，然后使用 NumPy 的 `meshgrid()` 函数创建 `R` 和 `P` 值的网格。最后，我们将使用 `Z` 方程来计算曲面上每个点的高度。

```python
r = np.linspace(0, 1.25, 50)
p = np.linspace(0, 2*np.pi, 50)
R, P = np.meshgrid(r, p)
Z = ((R**2 - 1)**2)
```
