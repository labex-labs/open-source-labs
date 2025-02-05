# 为每个样式表绘制演示图形

最后，你需要为每个可用的样式表绘制演示图形。你可以通过遍历 `style_list` 并为每个样式表调用 `plot_figure()` 函数来实现这一点。

```python
if __name__ == "__main__":

    # 设置一个按字母顺序排列的所有可用样式的列表，但
    # `default` 和 `classic` 样式将分别强制排在第一和第二位。
    # 带有前导下划线的样式用于内部使用，例如测试
    # 和绘图类型图库。这里将它们排除在外。
    style_list = ['default', 'classic'] + sorted(
        style for style in plt.style.available
        if style!= 'classic' and not style.startswith('_'))

    # 为每个可用的样式表绘制一个演示图形。
    for style_label in style_list:
        with plt.rc_context({"figure.max_open_warning": len(style_list)}):
            with plt.style.context(style_label):
                plot_figure(style_label=style_label)

    plt.show()
```
