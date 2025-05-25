# 각도 주석 화살표 및 텍스트 추가

각 브래킷 화살표 스타일에 각도 주석 화살표와 텍스트를 추가합니다. 먼저, *angleA*와 *angleB*에서 그려진 패치의 상단 좌표를 얻습니다. 그런 다음, 주석 화살표의 연결 방향을 정의합니다. 마지막으로, 플롯에 화살표와 주석 텍스트를 추가합니다.

```python
    # Get the top coordinates for the drawn patches at A and B
    patch_tops = [get_point_of_rotated_vertical(center, 0.5, angle)
                  for center, angle in zip(arrow_centers, anglesAB)]
    # Define the connection directions for the annotation arrows
    connection_dirs = (1, -1) if angle > 0 else (-1, 1)
    # Add arrows and annotation text
    arrowstyle = "Simple, tail_width=0.5, head_width=4, head_length=8"
    for vline, dir, patch_top, angle in zip(vlines, connection_dirs,
                                            patch_tops, anglesAB):
        kw = dict(connectionstyle=f"arc3,rad={dir * 0.5}",
                  arrowstyle=arrowstyle, color="C0")
        ax.add_patch(FancyArrowPatch(vline, patch_top, **kw))
        ax.text(vline[0] - dir * 0.15, y + 0.7, f'{angle}°', ha="center",
                va="center")
```
