# 특정 데이터 범위 검토하기

때로는 이미지 내의 특정 데이터 범위를 검토해야 할 필요가 있을 수 있습니다. `imshow` 함수에서 `clim` 매개변수를 사용하여 컬러맵의 범위를 조정함으로써 이를 수행할 수 있습니다. 이를 통해 이미지의 특정 영역에 집중하면서 다른 영역의 세부 사항을 희생할 수 있습니다.

```python
min_value, max_value = 100, 200
plt.imshow(img, clim=(min_value, max_value))
```
