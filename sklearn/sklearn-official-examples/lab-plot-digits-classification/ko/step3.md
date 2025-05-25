# 데이터셋 준비

이미지를 평탄화하여 각 2 차원 회색조 값 배열의 모양을 `(8, 8)`에서 `(64,)`로 바꿔야 합니다. 이렇게 하면 `(n_samples, n_features)` 모양의 데이터셋이 생성됩니다. 여기서 `n_samples`는 이미지 수이고 `n_features`는 각 이미지의 총 픽셀 수입니다.

```python
n_samples = len(digits.images)
data = digits.images.reshape((n_samples, -1))
```
