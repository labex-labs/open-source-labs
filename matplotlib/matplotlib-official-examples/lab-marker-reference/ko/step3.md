# 마커 채우기 스타일 (Marker Fill Styles)

채워진 마커의 테두리 색상과 채우기 색상은 개별적으로 지정할 수 있습니다. 또한, `fillstyle`은 채워지지 않음 (unfilled), 완전히 채워짐 (fully filled), 또는 다양한 방향으로 반만 채워짐 (half-filled) 으로 구성할 수 있습니다. 반만 채워진 스타일은 보조 채우기 색상으로 `markerfacecoloralt`를 사용합니다. 다음 코드는 마커 채우기 스타일을 만드는 방법을 보여줍니다.

```python
fig, ax = plt.subplots()
fig.suptitle('Marker fillstyle', fontsize=14)
fig.subplots_adjust(left=0.4)

filled_marker_style = dict(marker='o', linestyle=':', markersize=15,
                           color='darkgrey',
                           markerfacecolor='tab:blue',
                           markerfacecoloralt='lightsteelblue',
                           markeredgecolor='brown')

for y, fill_style in enumerate(Line2D.fillStyles):
    ax.text(-0.5, y, repr(fill_style), **text_style)
    ax.plot([y] * 3, fillstyle=fill_style, **filled_marker_style)
format_axes(ax)
```
