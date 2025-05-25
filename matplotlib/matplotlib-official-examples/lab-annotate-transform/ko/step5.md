# 주석 추가

마지막 단계는 플롯에 주석을 추가하는 것입니다. `ax.annotate` 메서드를 사용하여 텍스트와 화살표를 플롯에 추가합니다. 또한 주석의 스타일을 지정하기 위해 `bbox` 및 `arrowprops` 매개변수를 사용합니다.

```python
bbox = dict(boxstyle="round", fc="0.8")
arrowprops = dict(
    arrowstyle="->",
    connectionstyle="angle,angleA=0,angleB=90,rad=10")

offset = 72
ax.annotate(
    f'data = ({xdata:.1f}, {ydata:.1f})',
    (xdata, ydata),
    xytext=(-2*offset, offset), textcoords='offset points',
    bbox=bbox, arrowprops=arrowprops)
ax.annotate(
    f'display = ({xdisplay:.1f}, {ydisplay:.1f})',
    xy=(xdisplay, ydisplay), xycoords='figure pixels',
    xytext=(0.5*offset, -offset), textcoords='offset points',
    bbox=bbox, arrowprops=arrowprops)
```
