# Ajouter des colonnes au TreeView

Dans cette étape, nous allons ajouter des colonnes au TreeView qui afficheront nos données.

```python
def add_columns(self):
    for i in range(self.num_cols):
        column = Gtk.TreeViewColumn(str(i), Gtk.CellRendererText(), text=i)
        self.treeview.append_column(column)
```
