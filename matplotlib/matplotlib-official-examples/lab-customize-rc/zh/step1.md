# 创建一个设置默认参数的函数

要创建一个为图形设置默认参数的函数，你可以使用 `rcParams.update()` 方法。此方法接受一个参数名称和值的字典，并用新值更新当前的默认值。以下是一个为发布图形设置一些默认参数的函数示例：

```python
def set_pub():
    rcParams.update({
        "font.weight": "bold",  # 粗体字体
        "tick.labelsize": 15,   # 较大的刻度标签
        "lines.linewidth": 1,   # 粗线条
        "lines.color": "k",     # 黑色线条
        "grid.color": "0.5",    # 灰色网格线
        "grid.linestyle": "-",  # 实线网格线
        "grid.linewidth": 0.5,  # 细网格线
        "savefig.dpi": 300,     # 更高分辨率输出。
    })
```
