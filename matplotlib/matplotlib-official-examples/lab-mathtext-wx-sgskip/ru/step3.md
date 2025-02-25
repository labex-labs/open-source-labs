# Преобразование текста с математическими символами в wx.Bitmap

Определите функцию, которая преобразует текст с математическими символами в wx.Bitmap. Эта функция использует Matplotlib для рисования текста в позиции (0, 0), а затем relies на `facecolor="none"` и `bbox_inches="tight", pad_inches=0` для получения прозрачной маски, которая затем загружается в wx.Bitmap.

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
