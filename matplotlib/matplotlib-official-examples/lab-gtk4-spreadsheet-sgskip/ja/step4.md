# ツリービューに列を追加する

データを表示するために、ツリービューに列を追加する必要があります。

```python
    def add_columns(self):
        for i in range(self.num_cols):
            column = Gtk.TreeViewColumn(str(i), Gtk.CellRendererText(), text=i)
            self.treeview.append_column(column)
```
