# 创建数据

下一步是为三维表面创建数据。我们需要定义 `u`、`v`、`x`、`y` 和 `z`。这些变量将表示绘制表面所需的角度和坐标。使用 NumPy 的 `linspace()` 函数创建角度，使用 `outer()` 函数创建坐标。

```python
# 生成数据
u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, np.pi, 100)
x = 10 * np.outer(np.cos(u), np.sin(v))
y = 10 * np.outer(np.sin(u), np.sin(v))
z = 10 * np.outer(np.ones(np.size(u)), np.cos(v))
```
