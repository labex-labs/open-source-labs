# 컬러 스케일 참조 추가하기

컬러 스케일에 대한 참조를 제공하기 위해, 플롯에 컬러 바 (color bar) 를 추가할 수 있습니다. 이는 `matplotlib.pyplot`의 `colorbar` 함수를 사용하여 수행할 수 있습니다.

```python
imgplot = plt.imshow(lum_img)
plt.colorbar()
```
