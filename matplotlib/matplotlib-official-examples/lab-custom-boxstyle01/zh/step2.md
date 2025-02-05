# 将自定义框样式实现为类

自定义框样式也可以实现为实现了 `__call__` 方法的类。然后可以将这些类注册到 `BoxStyle._style_list` 字典中，这样就可以将框样式指定为字符串，即 `bbox=dict(boxstyle="已注册的名称,参数=值,...",...)`。

```python
class MyStyle:
    """一个简单的框。"""

    def __init__(self, pad=0.3):
        """
        参数必须是浮点数且有默认值。

        参数
        ----------
        pad : float
            填充量
        """
        self.pad = pad
        super().__init__()

    def __call__(self, x0, y0, width, height, mutation_size):
        """
        给定框的位置和大小，返回围绕它的框的路径。

        旋转会自动处理。

        参数
        ----------
        x0, y0, width, height : float
            框的位置和大小。
        mutation_size : float
            变形的参考比例，通常是文本字体大小。
        """
        # 填充
        pad = mutation_size * self.pad
        # 添加填充后的宽度和高度
        width = width + 2.*pad
        height = height + 2.*pad
        # 填充后框的边界
        x0, y0 = x0 - pad, y0 - pad
        x1, y1 = x0 + width, y0 + height
        # 返回新路径
        return Path([(x0, y0),
                     (x1, y0), (x1, y1), (x0, y1),
                     (x0-pad, (y0+y1)/2.), (x0, y0),
                     (x0, y0)],
                    closed=True)


BoxStyle._style_list["angled"] = MyStyle  # 注册自定义样式。

fig, ax = plt.subplots(figsize=(3, 3))
ax.text(0.5, 0.5, "Test", size=30, va="center", ha="center", rotation=30,
        bbox=dict(boxstyle="angled,pad=0.5", alpha=0.2))

del BoxStyle._style_list["angled"]  # 取消注册。

plt.show()
```
