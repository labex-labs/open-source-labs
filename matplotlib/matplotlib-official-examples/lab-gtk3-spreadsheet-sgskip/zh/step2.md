# 创建数据管理器窗口

在这一步中，我们将创建一个继承自 `Gtk.Window` 类的 `DataManager` 类。这个类将负责管理我们想要绘制的数据。

```python
class DataManager(Gtk.Window):
    num_rows, num_cols = 20, 10
    data = random((num_rows, num_cols))
```
