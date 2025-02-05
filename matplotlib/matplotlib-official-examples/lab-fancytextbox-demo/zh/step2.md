# 创建一个文本框

```python
plt.text(0.6, 0.7, "eggs", size=50, rotation=30.,
         ha="center", va="center",
         bbox=dict(boxstyle="round",
                   ec=(1., 0.5, 0.5),
                   fc=(1., 0.8, 0.8),
                   )
         )
```

我们使用 `text()` 方法创建了一个包含单词“eggs”的文本框。`bbox` 参数用于设置文本框的样式。`boxstyle` 参数设置为“round”以创建一个圆角框，而 `ec` 和 `fc` 参数分别设置框的边缘颜色和填充颜色。`size` 参数设置字体大小，`rotation` 参数设置旋转角度，`ha` 和 `va` 参数设置文本在框内的水平和垂直对齐方式。
