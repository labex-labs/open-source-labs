# 데모 이미지 가져오기

이 단계에서는 데모 이미지와 해당 범위를 가져오는 함수를 정의합니다. `cbook`의 `get_sample_data()` 함수를 사용하여 샘플 이미지를 가져옵니다.

```python
def get_demo_image():
    z = cbook.get_sample_data("axes_grid/bivariate_normal.npy")  # 15x15 array
    return z, (-3, 4, -4, 3)
```
