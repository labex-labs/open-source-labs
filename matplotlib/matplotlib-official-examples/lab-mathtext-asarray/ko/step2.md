# 텍스트를 RGBA 로 변환

텍스트를 이미지로 변환하기 위해, 빈 투명 figure 에 텍스트를 그리고, figure 를 임시 버퍼에 저장한 다음, `plt.imread`를 사용하여 버퍼를 로드합니다.

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
