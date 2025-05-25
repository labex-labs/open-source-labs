# 컬러바 추가

`inset_axes` 함수를 사용하여 삽입 축에 컬러바 (colorbar) 를 추가합니다. 컬러바의 너비 (width), 높이 (height), 위치 (location), 그리고 경계 상자 (bounding box) 를 설정합니다.

```python
cax = inset_axes(axins,
                 width="5%",  # width = 10% of parent_bbox width
                 height="100%",  # height : 50%
                 loc='lower left',
                 bbox_to_anchor=(1.05, 0., 1, 1),
                 bbox_transform=axins.transAxes,
                 borderpad=0,
                 )
fig.colorbar(im, cax=cax)
```
