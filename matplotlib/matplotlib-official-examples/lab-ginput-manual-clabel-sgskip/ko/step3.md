# 확대/축소 (Zoom)

이 단계에서는 플롯을 확대/축소합니다. `ginput` 함수를 사용하여 확대/축소 상자의 두 모서리를 선택하고, `waitforbuttonpress` 함수를 사용하여 확대/축소를 완료합니다.

```python
tellme('Now do a nested zoom, click to begin')
plt.waitforbuttonpress()

while True:
    tellme('Select two corners of zoom, middle mouse button to finish')
    pts = plt.ginput(2, timeout=-1)
    if len(pts) < 2:
        break
    (x0, y0), (x1, y1) = pts
    xmin, xmax = sorted([x0, x1])
    ymin, ymax = sorted([y0, y1])
    plt.xlim(xmin, xmax)
    plt.ylim(ymin, ymax)

tellme('All Done!')
plt.show()
```
