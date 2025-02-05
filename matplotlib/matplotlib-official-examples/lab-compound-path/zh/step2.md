# 创建顶点和代码

我们将为想要组合成复合路径的两个多边形创建顶点和代码。我们将使用 `Path.MOVETO` 将光标移动到多边形的起点，使用 `Path.LINETO` 从起点创建一条线到下一个点，并使用 `Path.CLOSEPOLY` 闭合多边形。

```python
vertices = []
codes = []

# 第一个多边形 - 矩形
codes = [Path.MOVETO] + [Path.LINETO]*3 + [Path.CLOSEPOLY]
vertices = [(1, 1), (1, 2), (2, 2), (2, 1), (0, 0)]

# 第二个多边形 - 三角形
codes += [Path.MOVETO] + [Path.LINETO]*2 + [Path.CLOSEPOLY]
vertices += [(4, 4), (5, 5), (5, 4), (0, 0)]
```
