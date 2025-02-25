# テキストをRGBAに変換する

テキストを画像に変換するには、空の透明な図に描画し、その図を一時バッファに保存し、次に`plt.imread`を使ってバッファを読み込みます。

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
