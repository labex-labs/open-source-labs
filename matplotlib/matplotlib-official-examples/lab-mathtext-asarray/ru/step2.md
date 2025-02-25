# Преобразуем текст в RGBA

Для преобразования текста в изображение мы нарисуем его на пустой и прозрачной фигуре, сохраним фигуру в временный буфер, а затем загрузим буфер с использованием `plt.imread`.

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
