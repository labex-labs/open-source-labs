# ImageGrid 에 이미지 표시

마지막으로, `imshow` 함수와 `zip` 함수를 사용하여 ImageGrid 에 이미지를 표시하고, 그리드의 축을 반복합니다.

```python
for ax, im in zip(grid, [im1, im2, im3]):
    ax.imshow(im, origin="lower", vmin=vmin, vmax=vmax)

plt.show()
```
