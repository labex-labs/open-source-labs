# 트리뷰에 열 추가

데이터를 표시하기 위해 트리뷰에 열을 추가해야 합니다.

```python
    def add_columns(self):
        for i in range(self.num_cols):
            column = Gtk.TreeViewColumn(str(i), Gtk.CellRendererText(), text=i)
            self.treeview.append_column(column)
```
