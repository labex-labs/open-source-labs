# 创建水平条形断裂图

在这一步中，我们将创建水平条形断裂图。我们将使用 `Axes` 类的 `broken_barh()` 方法来创建该图。`broken_barh()` 方法接受三个参数：第一个参数是一个元组列表，其中每个元组代表条形的一段，元组的第一个元素是该段的起始点，第二个元素是该段的长度；第二个参数是条形的 y 坐标；第三个参数是条形的填充颜色。

```python
fig, ax = plt.subplots()
ax.broken_barh([(110, 30), (150, 10)], (10, 9), facecolors='tab:blue')
ax.broken_barh([(10, 50), (100, 20), (130, 10)], (20, 9),
               facecolors=('tab:orange', 'tab:green', 'tab:red'))
ax.set_ylim(5, 35)
ax.set_xlim(0, 200)
ax.set_xlabel('seconds since start')
ax.set_yticks([15, 25], labels=['Bill', 'Jim'])
ax.grid(True)
ax.annotate('race interrupted', (61, 25),
            xytext=(0.8, 0.9), textcoords='axes fraction',
            arrowprops=dict(facecolor='black', shrink=0.05),
            fontsize=16,
            horizontalalignment='right', verticalalignment='top')

plt.show()
```
