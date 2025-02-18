# Agregar columnas a la vista de árbol (treeview)

Necesitas agregar columnas a la vista de árbol (treeview) para mostrar los datos.

```python
    def add_columns(self):
        for i in range(self.num_cols):
            column = Gtk.TreeViewColumn(str(i), Gtk.CellRendererText(), text=i)
            self.treeview.append_column(column)
```
