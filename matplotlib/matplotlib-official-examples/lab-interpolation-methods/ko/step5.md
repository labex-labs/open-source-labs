# 이미지 표시

`imshow` 함수와 다양한 보간 방법 (interpolation methods) 을 사용하여 이미지를 표시합니다.

```python
for ax, interp_method in zip(axs.flat, methods):
    ax.imshow(grid, interpolation=interp_method, cmap='viridis')
    ax.set_title(str(interp_method))
```
