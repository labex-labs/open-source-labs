# 이미지를 플롯하는 함수 생성

이 단계에서는 이미지, 플롯 축 (plot axis), 그리고 변환 (transformation) 을 입력으로 받는 함수를 정의합니다. 이 함수는 지정된 변환을 사용하여 플롯 축에 이미지를 표시합니다. 또한, 이미지의 의도된 범위를 보여주기 위해 이미지 주변에 노란색 사각형을 표시합니다.

```python
def do_plot(ax, Z, transform):
    im = ax.imshow(Z, interpolation='none',
                   origin='lower',
                   extent=[-2, 4, -3, 2], clip_on=True)

    trans_data = transform + ax.transData
    im.set_transform(trans_data)

    # display intended extent of the image
    x1, x2, y1, y2 = im.get_extent()
    ax.plot([x1, x2, x2, x1, x1], [y1, y1, y2, y2, y1], "y--",
            transform=trans_data)
    ax.set_xlim(-5, 5)
    ax.set_ylim(-4, 4)
```
