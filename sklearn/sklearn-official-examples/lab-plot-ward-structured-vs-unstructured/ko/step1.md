# 데이터 생성

Scikit-learn 의 `make_swiss_roll` 함수를 사용하여 Swiss Roll 데이터셋을 생성합니다. Swiss Roll 데이터셋은 나선형 모양의 3 차원 데이터셋입니다.

```python
from sklearn.datasets import make_swiss_roll

n_samples = 1500
noise = 0.05
X, _ = make_swiss_roll(n_samples, noise=noise)
# 더 얇게 만듭니다.
X[:, 1] *= 0.5
```
