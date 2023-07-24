# Define ItemProperties class

Next, we define a `ItemProperties` class which will be used to set the properties for each menu item. We can set the font size, label color, background color, and alpha value for each item using this class.

```python
class ItemProperties:
    def __init__(self, fontsize=14, labelcolor='black', bgcolor='yellow',
                 alpha=1.0):
        self.fontsize = fontsize
        self.labelcolor = labelcolor
        self.bgcolor = bgcolor
        self.alpha = alpha
```
