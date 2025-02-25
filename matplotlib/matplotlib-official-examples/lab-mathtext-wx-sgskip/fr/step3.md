# Convertir du texte mathématique en wx.Bitmap

Définissez une fonction qui convertit du texte mathématique en un wx.Bitmap. Cette fonction utilise Matplotlib pour tracer le texte à la position (0, 0), puis elle dépend de `facecolor="none"` et `bbox_inches="tight", pad_inches=0` pour obtenir un masque transparent qui est ensuite chargé dans un wx.Bitmap.

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
