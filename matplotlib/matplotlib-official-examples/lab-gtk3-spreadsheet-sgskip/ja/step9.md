# ツリービューに列を追加する

このステップでは、データを表示するための列をツリービューに追加します。

```python
def add_columns(self):
    for i in range(self.num_cols):
        column = Gtk.TreeViewColumn(str(i), Gtk.CellRendererText(), text=i)
        self.treeview.append_column(column)
```
