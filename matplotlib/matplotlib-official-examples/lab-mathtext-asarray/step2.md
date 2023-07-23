# Convert text to RGBA

To convert text to an image, we will draw it on an empty and transparent figure, save the figure to a temporary buffer, and then load the buffer using `plt.imread`.

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
