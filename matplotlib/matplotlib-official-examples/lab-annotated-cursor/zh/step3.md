# 创建带注释的游标类

我们创建一个新类`AnnotatedCursor`，它继承自`matplotlib.widgets.Cursor`，并展示了新窗口小部件的创建及其事件回调。`AnnotatedCursor`类用于创建一个带有显示当前坐标文本的十字准线游标。

```python
class AnnotatedCursor(Cursor):
    """
    A crosshair cursor like `~matplotlib.widgets.Cursor` with a text showing \
    the current coordinates.
   ...
    """
```
