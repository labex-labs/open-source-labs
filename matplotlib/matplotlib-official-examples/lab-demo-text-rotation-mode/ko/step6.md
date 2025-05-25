# 텍스트의 경계 상자 강조 표시

`rotation_mode`가 `'default'`로 설정된 경우, 사각형을 사용하여 텍스트의 경계 상자를 강조 표시합니다. `get_window_extent` 함수를 사용하여 경계 상자를 가져오고, `transData` 속성을 사용하여 데이터 좌표로 변환합니다.

```python
if mode == "default":
    fig.canvas.draw()
    for ax, text in texts.items():
        bb = text.get_window_extent().transformed(ax.transData.inverted())
        rect = plt.Rectangle((bb.x0, bb.y0), bb.width, bb.height,
                             facecolor="C1", alpha=0.3, zorder=2)
        ax.add_patch(rect)
```
