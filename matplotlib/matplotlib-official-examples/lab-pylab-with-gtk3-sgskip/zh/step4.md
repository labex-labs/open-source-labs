# 向工具栏添加按钮

我们将使用 Gtk 模块向工具栏添加一个按钮。首先，我们创建一个带有标签的按钮，并将其连接到一个函数，以便在点击时打印一条消息。然后，我们创建一个工具项，设置其工具提示文本，将按钮添加到其中，并将其插入到工具栏中。

```python
button = Gtk.Button(label='Click me')
button.show()
button.connect('clicked', lambda button: print('hi mom'))

toolitem = Gtk.ToolItem()
toolitem.show()
toolitem.set_tooltip_text('Click me for fun and profit')
toolitem.add(button)

pos = 8  # 在此处插入工具栏的位置
toolbar.insert(toolitem, pos)
```
