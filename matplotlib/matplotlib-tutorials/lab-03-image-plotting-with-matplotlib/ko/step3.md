# 의사 컬러 (Pseudocolor) 스킴 적용하기

의사 컬러 스킴은 대비를 향상시키고 데이터를 더 쉽게 시각화하는 데 사용할 수 있습니다. 이미지가 흑백인 경우, 다양한 컬러맵 (colormap) 을 지정하여 의사 컬러 스킴을 적용할 수 있습니다. `imshow` 함수에서 `cmap` 매개변수를 사용하여 이를 수행할 수 있습니다.

```python
lum_img = img[:, :, 0]
plt.imshow(lum_img, cmap="hot")
```
