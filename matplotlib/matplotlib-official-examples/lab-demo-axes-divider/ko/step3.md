# 간단한 이미지와 컬러바

이 단계에서는 간단한 이미지와 해당 컬러바를 생성합니다. 이미지를 생성하기 위해 `pyplot`의 `imshow()` 함수를 사용하고, 컬러바를 생성하기 위해 `colorbar()` 함수를 사용합니다.

```python
def demo_simple_image(ax):
    Z, extent = get_demo_image()

    im = ax.imshow(Z, extent=extent)
    cb = plt.colorbar(im)
    cb.ax.yaxis.set_tick_params(labelright=False)
```
