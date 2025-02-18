# Ajouter des colonnes à la vue d'arbre (treeview)

Vous devez ajouter des colonnes à la vue d'arbre pour afficher les données.

```python
    def add_columns(self):
        for i in range(self.num_cols):
            column = Gtk.TreeViewColumn(str(i), Gtk.CellRendererText(), text=i)
            self.treeview.append_column(column)
```
