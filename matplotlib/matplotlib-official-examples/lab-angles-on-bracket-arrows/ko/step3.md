# 각도 주석이 있는 브래킷 화살표 생성

`FancyArrowPatch`를 사용하여 각도 주석이 있는 세 가지 브래킷 화살표 스타일을 생성합니다. 각 브래킷 화살표는 *angleA*와 *angleB*에 대해 서로 다른 각도 값을 갖습니다. 또한 각도 주석의 위치를 나타내기 위해 수직선을 추가합니다.

```python
style = ']-['
for i, angle in enumerate([-40, 0, 60]):
    y = 2*i
    arrow_centers = ((1, y), (5, y))
    vlines = ((1, y + 0.5), (5, y + 0.5))
    anglesAB = (angle, -angle)
    bracketstyle = f"{style}, angleA={anglesAB[0]}, angleB={anglesAB[1]}"
    bracket = FancyArrowPatch(*arrow_centers, arrowstyle=bracketstyle,
                              mutation_scale=42)
    ax.add_patch(bracket)
    ax.text(3, y + 0.05, bracketstyle, ha="center", va="bottom", fontsize=14)
    ax.vlines([line[0] for line in vlines], [y, y], [line[1] for line in vlines],
              linestyles="--", color="C0")
```
