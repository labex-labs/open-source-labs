# 创建路径

接下来，我们将为贝塞尔曲线创建 `Path` 对象。`Path` 对象接受一个顶点列表和代码，这些代码指定了顶点之间的路径类型。在这种情况下，我们将使用 `MOVETO` 代码移动到起点，然后使用两个 `CURVE3` 代码指定控制点和终点，最后使用 `CLOSEPOLY` 代码闭合路径。

```python
Path = mpath.Path

bezier_path = Path([(0, 0), (1, 0), (1, 1), (0, 0)],
                   [Path.MOVETO, Path.CURVE3, Path.CURVE3, Path.CLOSEPOLY])
```
