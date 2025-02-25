# Добавьте столбцы в TreeView

В этом шаге мы добавим столбцы в TreeView, которые будут отображать наши данные.

```python
def add_columns(self):
    for i in range(self.num_cols):
        column = Gtk.TreeViewColumn(str(i), Gtk.CellRendererText(), text=i)
        self.treeview.append_column(column)
```
