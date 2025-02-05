# 向 TreeView 添加列

在这一步中，我们将向 TreeView 添加列，用于显示我们的数据。

```python
def add_columns(self):
    for i in range(self.num_cols):
        column = Gtk.TreeViewColumn(str(i), Gtk.CellRendererText(), text=i)
        self.treeview.append_column(column)
```
