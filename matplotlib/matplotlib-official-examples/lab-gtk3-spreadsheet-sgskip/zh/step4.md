# 添加一个标签

在这一步中，我们将向窗口添加一个标签，提示用户双击某一行来绘制数据。

```python
vbox = Gtk.VBox(homogeneous=False, spacing=8)
self.add(vbox)
label = Gtk.Label(label='Double click a row to plot the data')
vbox.pack_start(label, False, False, 0)
```
