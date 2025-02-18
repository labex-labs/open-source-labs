# Добавление столбцов в древовидное представление (treeview)

Вам нужно добавить столбцы в древовидное представление (treeview), чтобы отобразить данные.

```python
    def add_columns(self):
        for i in range(self.num_cols):
            column = Gtk.TreeViewColumn(str(i), Gtk.CellRendererText(), text=i)
            self.treeview.append_column(column)
```
