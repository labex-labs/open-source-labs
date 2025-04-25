# 创建带空洞的填充等高线

如 Path 类中所述，可以在多边形顶点的单个列表中指定多个填充等高线，并附带顶点类型（代码类型）列表。这对于带有空洞的多边形特别有用。

```python
fig, ax = plt.subplots()
filled01 = [[[0, 0], [3, 0], [3, 3], [0, 3], [1, 1], [1, 2], [2, 2], [2, 1]]]
M = Path.MOVETO
L = Path.LINETO
kinds01 = [[M, L, L, L, M, L, L, L]]
cs = ContourSet(ax, [0, 1], [filled01], [kinds01], filled=True)
cbar = fig.colorbar(cs)

ax.set(xlim=(-0.5, 3.5), ylim=(-0.5, 3.5),
       title='用户指定的带空洞的填充等高线')
```
