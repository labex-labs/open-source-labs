# 이미지 데이터 정의

샘플 이미지 데이터와 해당 범위를 반환하는 함수를 정의합니다.

```python
def get_demo_image():
    z = cbook.get_sample_data("axes_grid/bivariate_normal.npy")  # 15x15 array
    return z, (-3, 4, -4, 3)
```
