# 设置窗口

在这一步中，我们将设置用于显示数据的窗口。我们首先用一个标题和一个大小来初始化窗口。

```python
def __init__(self):
    super().__init__()
    self.set_default_size(600, 600)
    self.connect('destroy', lambda win: Gtk.main_quit())
    self.set_title('GtkListStore demo')
    self.set_border_width(8)
```
