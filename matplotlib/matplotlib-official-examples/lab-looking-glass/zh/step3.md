# 创建图形和坐标轴

我们将使用 `subplots()` 函数创建图形和坐标轴对象。我们还将使用 `patches.Circle()` 函数向坐标轴对象添加一个黄色的圆形补丁。

```python
fig, ax = plt.subplots()
circ = patches.Circle((0.5, 0.5), 0.25, alpha=0.8, fc='yellow')
ax.add_patch(circ)
```
