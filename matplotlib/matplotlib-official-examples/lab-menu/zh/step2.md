# 定义ItemProperties类

接下来，我们定义一个`ItemProperties`类，该类将用于设置每个菜单项的属性。使用这个类，我们可以为每个菜单项设置字体大小、标签颜色、背景颜色和透明度值。

```python
class ItemProperties:
    def __init__(self, fontsize=14, labelcolor='black', bgcolor='yellow',
                 alpha=1.0):
        self.fontsize = fontsize
        self.labelcolor = labelcolor
        self.bgcolor = bgcolor
        self.alpha = alpha
```
