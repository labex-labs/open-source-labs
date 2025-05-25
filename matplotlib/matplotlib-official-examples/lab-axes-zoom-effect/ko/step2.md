# 축 간의 연결 정의

이 단계에서는 두 축 사이의 연결을 정의합니다. 이 함수는 두 개의 축을 입력으로 받으며, x 축의 최소값과 최대값을 입력으로 받습니다. 그런 다음 경계 상자 (bounding box) 를 생성하고 두 축을 연결합니다.

```python
def zoom_effect01(ax1, ax2, xmin, xmax, **kwargs):
    bbox = Bbox.from_extents(xmin, 0, xmax, 1)

    mybbox1 = TransformedBbox(bbox, ax1.get_xaxis_transform())
    mybbox2 = TransformedBbox(bbox, ax2.get_xaxis_transform())

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
