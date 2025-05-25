# Mathtext 를 wx.Bitmap 으로 변환

mathtext 를 wx.Bitmap 으로 변환하는 함수를 정의합니다. 이 함수는 Matplotlib 을 사용하여 (0, 0) 위치에 텍스트를 그리지만, `facecolor="none"`과 `bbox_inches="tight", pad_inches=0`을 사용하여 투명 마스크를 얻은 다음 wx.Bitmap 에 로드합니다.

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
