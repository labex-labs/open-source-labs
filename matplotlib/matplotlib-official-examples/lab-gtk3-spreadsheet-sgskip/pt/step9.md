# Adicionar Colunas à TreeView

Nesta etapa, adicionaremos colunas à treeview que exibirão nossos dados.

```python
def add_columns(self):
    for i in range(self.num_cols):
        column = Gtk.TreeViewColumn(str(i), Gtk.CellRendererText(), text=i)
        self.treeview.append_column(column)
```
