# TreeView 에 열 추가

이 단계에서는 데이터를 표시할 열을 treeview 에 추가합니다.

```python
def add_columns(self):
    for i in range(self.num_cols):
        column = Gtk.TreeViewColumn(str(i), Gtk.CellRendererText(), text=i)
        self.treeview.append_column(column)
```
