# 합성 데이터셋 생성

`X`와 `y`가 선형적으로 연결된 합성 데이터셋을 생성합니다. `X`의 10 개 특징이 `y`를 생성하는 데 사용됩니다. 다른 특징들은 `y`를 예측하는 데 유용하지 않습니다. 또한, `n_samples == n_features`인 데이터셋을 생성합니다. 이러한 설정은 OLS 모델에 어려움을 주며, 잠재적으로 임의로 큰 가중치를 초래할 수 있습니다. 가중치에 사전 정보를 제공하고 페널티를 적용하면 이 문제를 완화할 수 있습니다. 마지막으로 가우시안 노이즈가 추가됩니다.

```python
from sklearn.datasets import make_regression

X, y, true_weights = make_regression(
    n_samples=100,
    n_features=100,
    n_informative=10,
    noise=8,
    coef=True,
    random_state=42,
)
```
