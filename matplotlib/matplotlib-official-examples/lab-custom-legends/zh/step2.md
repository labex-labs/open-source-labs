# 编写自定义图例

在这一步中，我们将使用 Matplotlib 对象创建一个自定义图例。首先，我们从 `matplotlib.lines` 模块中导入 `Line2D` 类。接下来，我们创建一个包含 `Line2D` 对象的列表，并为其设置自定义的颜色、宽度和标签属性。最后，我们再次使用 `plot` 函数绘制数据，并使用自定义线条和相应标签调用 `legend()`。

```python
# 导入Line2D类
from matplotlib.lines import Line2D

# 创建自定义线条
custom_lines = [Line2D([0], [0], color=cmap(0.), lw=4),
                Line2D([0], [0], color=cmap(.5), lw=4),
                Line2D([0], [0], color=cmap(1.), lw=4)]

# 绘制数据并生成自定义图例
fig, ax = plt.subplots()
lines = ax.plot(data)
ax.legend(custom_lines, ['Cold', 'Medium', 'Hot'])
```
