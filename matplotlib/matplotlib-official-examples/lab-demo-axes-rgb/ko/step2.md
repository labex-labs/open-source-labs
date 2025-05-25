# RGB 채널을 얻는 함수 정의

이 단계에서는 이미지의 R, G, B 채널을 얻기 위해 `get_rgb()` 함수를 정의합니다. 이 예제에서는 `cbook` 모듈의 `get_sample_data()` 함수를 사용하여 샘플 이미지를 가져옵니다.

```python
import matplotlib.cbook as cbook

def get_rgb():
    # Get a sample image
    Z = cbook.get_sample_data("axes_grid/bivariate_normal.npy")
    Z[Z < 0] = 0.
    Z = Z / Z.max()

    # Get R, G, and B channels
    R = Z[:13, :13]
    G = Z[2:, 2:]
    B = Z[:13, 2:]

    return R, G, B
```
