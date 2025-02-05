# 设置菜单项

我们定义一个函数，该函数根据所选的颜色滤镜名称设置菜单项。此函数会根据所选内容更新颜色滤镜函数。

```python
def _set_menu_entry(tb, name):
    tb.canvas.figure.set_agg_filter(_get_color_filter(name))
    tb.canvas.draw_idle()
```
