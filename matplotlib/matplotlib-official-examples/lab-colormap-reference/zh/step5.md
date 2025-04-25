# 创建自定义颜色映射表

Matplotlib 还提供了创建自定义颜色映射表的功能。当内置颜色映射表无法提供所需的数据表示时，这会很有用。

```python
import matplotlib.colors as mcolors

# 定义颜色及其对应值的列表
colors = [(0,'red'), (0.5, 'green'), (1, 'blue')]

# 根据颜色列表创建一个 LinearSegmentedColormap 对象
cmap = mcolors.LinearSegmentedColormap.from_list('my_cmap', colors)
```
