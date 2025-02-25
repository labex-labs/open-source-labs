# Spalten zur TreeView hinzufügen

In diesem Schritt fügen wir Spalten zur TreeView hinzu, die unsere Daten anzeigen werden.

```python
def add_columns(self):
    for i in range(self.num_cols):
        column = Gtk.TreeViewColumn(str(i), Gtk.CellRendererText(), text=i)
        self.treeview.append_column(column)
```
