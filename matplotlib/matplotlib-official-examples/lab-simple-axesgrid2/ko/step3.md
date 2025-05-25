# 이미지 데이터 로드

ImageGrid 를 시연하기 위해 `cbook`에서 제공하는 `bivariate_normal.npy`라는 예시 이미지 데이터를 사용합니다. `cbook`의 `get_sample_data` 함수를 사용하여 이미지 데이터를 로드합니다.

```python
Z = cbook.get_sample_data("axes_grid/bivariate_normal.npy")
im1 = Z
im2 = Z[:, :10]
im3 = Z[:, 10:]
vmin, vmax = Z.min(), Z.max()
```
