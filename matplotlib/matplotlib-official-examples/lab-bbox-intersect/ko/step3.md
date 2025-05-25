# 임의의 선 생성

`numpy` 라이브러리를 사용하여 12 개의 임의의 선을 생성하고, `plot` 메서드를 사용하여 플롯합니다. 선이 사각형과 교차하면 색상은 빨간색, 그렇지 않으면 파란색으로 표시됩니다. `Path` 클래스를 사용하여 선을 생성하고, `intersects_bbox` 메서드를 사용하여 사각형과 교차하는지 확인합니다.

```python
bbox = Bbox.from_bounds(left, bottom, width, height)

for i in range(12):
    vertices = (np.random.random((2, 2)) - 0.5) * 6.0
    path = Path(vertices)
    if path.intersects_bbox(bbox):
        color = 'r'
    else:
        color = 'b'
    ax.plot(vertices[:, 0], vertices[:, 1], color=color)
```
