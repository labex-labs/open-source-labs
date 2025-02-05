# 自定义绘图

第四步是通过添加图例、设置坐标轴范围和标签以及更改视角来自定义绘图。

```python
# 添加图例，设置坐标轴范围和标签
ax.legend()
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_zlim(0, 1)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# 自定义视角，以便更清楚地看到散点位于
# 平面 y=0 上
ax.view_init(elev=20., azim=-35, roll=0)

plt.show()
```
