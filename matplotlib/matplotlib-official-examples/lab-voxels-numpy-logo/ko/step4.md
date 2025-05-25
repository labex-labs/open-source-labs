# 복셀 이미지 업스케일링

이제 앞서 정의한 `explode` 함수를 사용하여 복셀 이미지를 업스케일링하고 각 복셀 사이에 간격을 둡니다.

```python
filled = np.ones(n_voxels.shape)
filled_2 = explode(filled)
fcolors_2 = explode(facecolors)
ecolors_2 = explode(edgecolors)
```
