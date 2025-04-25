# 使用不同的 Matplotlib 对象编写自定义图例

在这一步中，我们将使用不同的 Matplotlib 对象（包括`Line2D`和`Patch`）创建一个自定义图例。首先，我们从`matplotlib.patches`模块中导入`Patch`类。接下来，我们创建一个具有自定义属性的`Line2D`和`Patch`对象列表。最后，我们使用这些自定义对象和相应的标签调用`legend()`。

```python
# 导入 Line2D 和 Patch 类
from matplotlib.lines import Line2D
from matplotlib.patches import Patch

# 创建图例元素
legend_elements = [Line2D([0], [0], color='b', lw=4, label='Line'),
                   Line2D([0], [0], marker='o', color='w', label='Scatter',
                          markerfacecolor='g', markersize=15),
                   Patch(facecolor='orange', edgecolor='r',
                         label='Color Patch')]

# 绘制数据并生成自定义图例
fig, ax = plt.subplots()
ax.legend(handles=legend_elements, loc='center')
```
