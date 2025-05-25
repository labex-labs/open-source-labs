# 배열 보간 방식 (Array Interpolation Schemes)

이미지 크기를 조정할 때, 누락된 공간을 채우기 위해 픽셀 값을 보간해야 합니다. 주변 픽셀을 기반으로 픽셀의 값을 결정하기 위해 다양한 보간 방식 (interpolation schemes) 을 사용할 수 있습니다. Matplotlib 은 "nearest", "bilinear", "bicubic"과 같은 다양한 보간 옵션을 제공합니다.

```python
plt.imshow(img, interpolation="bilinear")
```
