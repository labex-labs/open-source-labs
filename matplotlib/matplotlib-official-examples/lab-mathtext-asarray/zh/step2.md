# 将文本转换为 RGBA

为了将文本转换为图像，我们将把它绘制在一个空白且透明的图形上，将该图形保存到一个临时缓冲区，然后使用 `plt.imread` 加载该缓冲区。

```python
def text_to_rgba(s, *, dpi, **kwargs):
    fig = Figure(facecolor="none")
    fig.text(0, 0, s, **kwargs)
    with BytesIO() as buf:
        fig.savefig(buf, dpi=dpi, format="png", bbox_inches="tight", pad_inches=0)
        buf.seek(0)
        rgba = plt.imread(buf)
    return rgba
```
