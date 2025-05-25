# 그라데이션 바 함수 정의

다음으로, 그라데이션 바를 생성하는 함수를 정의해야 합니다. 이 함수는 axes 객체, 바의 x 및 y 좌표, 바의 너비 및 바의 하단 위치를 입력으로 받습니다. 그런 다음 함수는 각 바에 대한 그라데이션 이미지를 생성하고 반환합니다.

```python
def gradient_bar(ax, x, y, width=0.5, bottom=0):
    for left, top in zip(x, y):
        right = left + width
        gradient_image(ax, extent=(left, right, bottom, top),
                       cmap=plt.cm.Blues_r, cmap_range=(0, 0.8))
```
