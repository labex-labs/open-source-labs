# 向画布添加标签

```python
label = Gtk.Label()
label.set_markup('Drag mouse over axes for position')
vbox.insert_child_after(label, fig.canvas)
```

我们创建一个标签并设置其文本。我们将标签添加到垂直框中图形画布之后的位置。
