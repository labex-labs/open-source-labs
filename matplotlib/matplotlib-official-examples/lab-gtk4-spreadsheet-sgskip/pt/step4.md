# Adicionar Colunas à Treeview

Você precisa adicionar colunas à treeview para exibir os dados.

```python
    def add_columns(self):
        for i in range(self.num_cols):
            column = Gtk.TreeViewColumn(str(i), Gtk.CellRendererText(), text=i)
            self.treeview.append_column(column)
```
