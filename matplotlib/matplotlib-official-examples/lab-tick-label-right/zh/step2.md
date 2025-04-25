# 将默认的 y 轴刻度标签设置在右侧

我们可以使用以下代码将默认的 y 轴刻度标签设置在绘图的右侧：

```python
plt.rcParams['ytick.right'] = plt.rcParams['ytick.labelright'] = True
plt.rcParams['ytick.left'] = plt.rcParams['ytick.labelleft'] = False
```
