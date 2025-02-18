# Spalten zur Treeview hinzufügen

Sie müssen Spalten zur Treeview (Baumansicht) hinzufügen, um die Daten anzuzeigen.

```python
    def add_columns(self):
        for i in range(self.num_cols):
            column = Gtk.TreeViewColumn(str(i), Gtk.CellRendererText(), text=i)
            self.treeview.append_column(column)
```
