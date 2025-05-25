# Converter Mathtext para wx.Bitmap

Defina uma função que converte texto matemático (mathtext) para um wx.Bitmap. Esta função usa Matplotlib para desenhar o texto na posição (0, 0), mas então se baseia em `facecolor="none"` e `bbox_inches="tight", pad_inches=0` para obter uma máscara transparente que é então carregada em um wx.Bitmap.

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
