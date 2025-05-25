# 데이터 준비

이 단계에서는 훈련 및 테스트 데이터를 준비합니다. `sklearn.datasets`의 `load_digits` 함수를 사용하여 데이터 세트를 가져옵니다. 그런 다음 각 방향으로 1 픽셀씩 선형 이동을 통해 훈련 데이터를 변형하여 레이블이 지정된 데이터를 인공적으로 5 배 더 생성합니다. 데이터를 0 과 1 사이로 스케일링합니다.

```python
import numpy as np
from scipy.ndimage import convolve
from sklearn import datasets
from sklearn.preprocessing import minmax_scale
from sklearn.model_selection import train_test_split

def nudge_dataset(X, Y):
    """
    이 함수는 X 의 8x8 이미지를 좌, 우, 하, 상으로 1 픽셀씩 이동하여 원본 데이터보다 5 배 큰 데이터 세트를 생성합니다.
    """
    direction_vectors = [
        [[0, 1, 0], [0, 0, 0], [0, 0, 0]],
        [[0, 0, 0], [1, 0, 0], [0, 0, 0]],
        [[0, 0, 0], [0, 0, 1], [0, 0, 0]],
        [[0, 0, 0], [0, 0, 0], [0, 1, 0]],
    ]

    def shift(x, w):
        return convolve(x.reshape((8, 8)), mode="constant", weights=w).ravel()

    X = np.concatenate(
        [X] + [np.apply_along_axis(shift, 1, X, vector) for vector in direction_vectors]
    )
    Y = np.concatenate([Y for _ in range(5)], axis=0)
    return X, Y

X, y = datasets.load_digits(return_X_y=True)
X = np.asarray(X, "float32")
X, Y = nudge_dataset(X, y)
X = minmax_scale(X, feature_range=(0, 1))  # 0-1 범위로 스케일링

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=0)
```
