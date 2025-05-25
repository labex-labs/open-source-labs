# 두 번째 확대 축 생성

이 단계에서는 두 번째 확대 축을 생성합니다. 이 함수는 두 개의 축을 입력으로 받습니다. 그런 다음 두 번째 축에 대한 경계 상자 (bounding box) 를 생성하고 이를 첫 번째 축에 연결합니다.

```python
def zoom_effect02(ax1, ax2, **kwargs):
    tt = ax1.transScale + (ax1.transLimits + ax2.transAxes)
    trans = blended_transform_factory(ax2.transData, tt)

    mybbox1 = ax1.bbox
    mybbox2 = TransformedBbox(ax1.viewLim, trans)

    prop_patches = {**kwargs, "ec": "none", "alpha": 0.2}

    c1, c2, bbox_patch1, bbox_patch2, p = connect_bbox(
        mybbox1, mybbox2,
        loc1a=3, loc2a=2, loc1b=4, loc2b=1,
        prop_lines=kwargs, prop_patches=prop_patches)

    ax1.add_patch(bbox_patch1)
    ax2.add_patch(bbox_patch2)
    ax2.add_patch(c1)
    ax2.add_patch(c2)
    ax2.add_patch(p)

    return c1, c2, bbox_patch1, bbox_patch2, p
```
