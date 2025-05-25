# 그리드 반복 및 이미지 플롯

그런 다음 `zip` 함수를 사용하여 `grid` 객체를 반복하여 축과 이미지 배열을 모두 반복합니다. `imshow` 함수를 사용하여 각 이미지를 해당 축에 플롯합니다.

```python
for ax, im in zip(grid, [im1, im2, im3, im4]):
    ax.imshow(im)
```
