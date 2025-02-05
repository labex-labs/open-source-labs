# 自定义绘图

我们可以通过为坐标轴添加标签并调整视角来定制绘图。

```python
ax.set_xlabel('X 标签')
ax.set_ylabel('Y 标签')
ax.set_zlabel('Z 标签')
ax.view_init(elev=30, azim=120)
```
