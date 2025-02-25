# 数式を wx.Bitmap に変換する

数式を wx.Bitmap に変換する関数を定義します。この関数は、Matplotlib を使って座標 (0, 0) にテキストを描画しますが、その後 `facecolor="none"` と `bbox_inches="tight", pad_inches=0` を使って透明なマスクを取得し、それを wx.Bitmap に読み込みます。

```python
def mathtext_to_wxbitmap(s):
    fig = Figure(facecolor="none")
    text_color = (
        np.array(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOWTEXT)) / 255)
    fig.text(0, 0, s, fontsize=10, color=text_color)
    buf = BytesIO()
    fig.savefig(buf, format="png", dpi=150, bbox_inches="tight", pad_inches=0)
    s = buf.getvalue()
    return wx.Bitmap.NewFromPNGData(s, len(s))
```
