# Convertir texto matemático a wx.Bitmap

Define una función que convierte texto matemático en un wx.Bitmap. Esta función utiliza Matplotlib para dibujar el texto en la posición (0, 0), pero luego se basa en `facecolor="none"` y `bbox_inches="tight", pad_inches=0` para obtener una máscara transparente que luego se carga en un wx.Bitmap.

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
