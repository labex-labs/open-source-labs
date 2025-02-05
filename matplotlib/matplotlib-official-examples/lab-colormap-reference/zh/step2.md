# 创建一个简单的颜色映射表

要创建一个简单的颜色映射表，我们可以使用 `matplotlib.colors` 模块中的 `ListedColormap` 类。这个类接受一个颜色列表，并根据它们创建一个颜色映射表。

```python
import matplotlib.colors as mcolors

# 定义一个颜色列表
colors = ['red', 'green', 'blue']

# 根据颜色列表创建一个 ListedColormap 对象
cmap = mcolors.ListedColormap(colors)
```
