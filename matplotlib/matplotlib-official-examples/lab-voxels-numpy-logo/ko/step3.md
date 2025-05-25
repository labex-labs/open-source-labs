# NumPy 로고 구성

이제 `n_voxels`라는 3D NumPy 배열을 사용하여 NumPy 로고를 구성할 수 있습니다. 로고의 모양을 나타내기 위해 배열의 특정 요소들을 True 로 설정합니다. 또한 복셀의 색상을 지정하는 데 사용될 `facecolors`와 `edgecolors`라는 두 개의 다른 NumPy 배열도 정의합니다.

```python
n_voxels = np.zeros((4, 3, 4), dtype=bool)
n_voxels[0, 0, :] = True
n_voxels[-1, 0, :] = True
n_voxels[1, 0, 2] = True
n_voxels[2, 0, 1] = True

facecolors = np.where(n_voxels, '#FFD65DC0', '#7A88CCC0')
edgecolors = np.where(n_voxels, '#BFAB6E', '#7D84A6')
```
