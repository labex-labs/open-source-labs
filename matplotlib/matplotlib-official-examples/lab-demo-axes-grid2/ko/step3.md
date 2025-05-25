# 샘플 데이터 준비

cbook 의 `get_sample_data` 함수를 사용하여 샘플 데이터를 얻습니다. 그런 다음 그리드에 표시할 이미지를 준비합니다.

```python
Z = cbook.get_sample_data("axes_grid/bivariate_normal.npy")
extent = (-3, 4, -4, 3)
ZS = [Z[i::3, :] for i in range(3)]
extent = extent[0], extent[1]/3., extent[2], extent[3]
```
