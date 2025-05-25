# 각 컬러맵에 대한 BboxImage 생성

다음으로, 각 컬러맵에 대한 BboxImage 를 생성합니다. `plt.colormaps` 메서드를 사용하여 모든 컬러맵의 목록을 생성하는 것으로 시작합니다. 그런 다음 컬러맵 목록을 반복하는 `for` 루프를 생성합니다. 각 컬러맵에 대해 `divmod()` 메서드를 사용하여 `ix` 및 `iy` 위치를 계산합니다. 그런 다음 `Bbox.from_bounds()` 메서드를 사용하여 `Bbox` 객체를 생성합니다. 경계 상자를 생성하기 위해 `ix`, `iy`, `dx` 및 `dy` 값을 `Bbox.from_bounds()` 메서드에 전달합니다. 그런 다음 `Bbox` 객체와 `ax2.transAxes` 객체를 사용하여 `TransformedBbox` 객체를 생성합니다. 마지막으로 `add_artist()` 메서드를 사용하여 `BboxImage` 객체를 생성합니다. 컬러맵으로 이미지를 생성하기 위해 `TransformedBbox` 객체를 `BboxImage` 생성자에 전달합니다.

```python
cmap_names = sorted(m for m in plt.colormaps if not m.endswith("_r"))

ncol = 2
nrow = len(cmap_names) // ncol + 1

xpad_fraction = 0.3
dx = 1 / (ncol + xpad_fraction * (ncol - 1))

ypad_fraction = 0.3
dy = 1 / (nrow + ypad_fraction * (nrow - 1))

for i, cmap_name in enumerate(cmap_names):
    ix, iy = divmod(i, nrow)
    bbox0 = Bbox.from_bounds(ix*dx*(1+xpad_fraction),
                             1 - iy*dy*(1+ypad_fraction) - dy,
                             dx, dy)
    bbox = TransformedBbox(bbox0, ax2.transAxes)
    ax2.add_artist(
        BboxImage(bbox, cmap=cmap_name, data=np.arange(256).reshape((1, -1))))
```
