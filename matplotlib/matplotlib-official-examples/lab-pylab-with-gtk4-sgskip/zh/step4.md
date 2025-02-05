# 向工具栏添加按钮

```python
button = Gtk.Button(label='Click me')
button.connect('clicked', lambda button: print('hi mom'))
button.set_tooltip_text('Click me for fun and profit')
toolbar.append(button)
```

我们创建一个带有标签和工具提示的按钮，并将其连接到一个向控制台打印消息的函数。我们将该按钮添加到工具栏。
