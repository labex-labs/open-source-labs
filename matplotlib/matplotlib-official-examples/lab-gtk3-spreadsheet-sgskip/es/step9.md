# Agregar columnas al TreeView

En este paso, agregaremos columnas al `TreeView` que mostrarán nuestros datos.

```python
def add_columns(self):
    for i in range(self.num_cols):
        column = Gtk.TreeViewColumn(str(i), Gtk.CellRendererText(), text=i)
        self.treeview.append_column(column)
```
