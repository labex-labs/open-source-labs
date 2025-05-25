# 데이터 그리드 준비

등고선 플롯을 위한 데이터 그리드를 설정할 것입니다. `construct_grids` 함수를 사용하여 이 작업을 수행할 것입니다.

```python
X, Y = np.meshgrid(xgrid[::5], ygrid[::5][::-1])
land_reference = data.coverages[6][::5, ::5]
land_mask = (land_reference > -9999).ravel()

xy = np.vstack([Y.ravel(), X.ravel()]).T
xy = xy[land_mask]
xy *= np.pi / 180.0
```
