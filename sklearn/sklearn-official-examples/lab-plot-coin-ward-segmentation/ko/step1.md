# 데이터 생성

데이터 생성부터 시작하겠습니다. scikit-image 의 `coins` 데이터셋을 사용할 것입니다. 이 데이터셋은 동전의 2 차원 회색조 이미지입니다. 처리 속도를 높이기 위해 이미지 크기를 원본 크기의 20% 로 줄일 것입니다.

```python
from skimage.data import coins
import numpy as np
from scipy.ndimage import gaussian_filter
from skimage.transform import rescale

orig_coins = coins()

# 처리 속도를 높이기 위해 원본 크기의 20% 로 크기를 조정합니다.
# 다운스케일 전에 가우시안 필터를 적용하여 부드럽게 하면
# 앨리어싱 아티팩트를 줄일 수 있습니다.

smoothened_coins = gaussian_filter(orig_coins, sigma=2)
rescaled_coins = rescale(
    smoothened_coins,
    0.2,
    mode="reflect",
    anti_aliasing=False,
)

X = np.reshape(rescaled_coins, (-1, 1))
```
