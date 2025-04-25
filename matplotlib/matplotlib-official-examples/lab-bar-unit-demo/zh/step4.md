# 定义柱状图参数

下一步是定义柱状图的参数。我们将定义组的 x 位置、柱子的宽度以及 x 轴刻度的标签。

```python
ind = np.arange(N)    # 组的 x 位置
width = 0.35         # 柱子的宽度
ax.set_xticks(ind + width / 2, labels=['G1', 'G2', 'G3', 'G4', 'G5'])
```
