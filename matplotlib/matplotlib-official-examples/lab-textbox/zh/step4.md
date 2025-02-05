# 创建文本框小部件

我们创建文本框小部件并将其添加到图形中。当用户在文本框中按下回车键或离开文本框时，`on_submit` 方法用于触发 `submit` 函数。我们还将文本框小部件的初始值设置为 `t ** 2`。

```python
axbox = fig.add_axes([0.1, 0.05, 0.8, 0.075])
text_box = TextBox(axbox, "Evaluate", textalignment="center")
text_box.on_submit(submit)
text_box.set_val("t ** 2")  # Trigger `submit` with the initial string.
```
