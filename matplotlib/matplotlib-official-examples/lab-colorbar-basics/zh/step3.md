# 创建正数数据图和颜色条

我们创建正数数据的图，并使用 `colorbar` 函数为该图添加颜色条。

```python
# 仅绘制正数数据，并保存 ax1.imshow 返回的颜色“可映射”对象
pos = plt.imshow(Zpos, cmap='Blues', interpolation='none')

# 使用图形的方法添加颜色条，指明我们所讨论的可映射对象以及它应靠近的轴对象
plt.colorbar(pos)
```
