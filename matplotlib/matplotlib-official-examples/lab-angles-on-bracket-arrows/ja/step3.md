# 角度注釈付きのブラケット矢印を作成する

`FancyArrowPatch` を使って、角度注釈付きの 3 種類のブラケット矢印スタイルを作成します。各ブラケット矢印は、_angleA_ と _angleB_ に対して異なる角度値を持ちます。また、角度注釈の位置を示すために垂直線も追加します。

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
