# Convert Mathtext to wx.Bitmap

Define a function that converts math text to a wx.Bitmap. This function uses Matplotlib to draw the text at position (0, 0) but then relies on `facecolor="none"` and `bbox_inches="tight", pad_inches=0` to get a transparent mask that is then loaded into a wx.Bitmap.

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
