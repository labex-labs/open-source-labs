# 向垂直框添加标签

我们将向垂直框添加一个标签，用于在鼠标在坐标轴上拖动时显示其 x、y 坐标。首先，我们创建一个带有一些文本的标签，并将其添加到垂直框中。

```python
label = Gtk.Label()
label.set_markup('Drag mouse over axes for position')
label.show()
vbox.pack_start(label, False, False, 0)
```
