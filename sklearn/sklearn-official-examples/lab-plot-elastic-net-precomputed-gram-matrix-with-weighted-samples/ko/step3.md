# 탄성 네트워크 적합

이제 적합을 진행할 수 있습니다. 탄성 네트워크 추정자가 중심이 맞춰지지 않았음을 감지하고 우리가 전달한 그램 행렬을 버리는 것을 방지하기 위해 중심에 맞춘 설계 행렬을 `fit`에 전달해야 합니다. 그러나 조정된 설계 행렬을 전달하면 전처리 코드가 두 번째로 잘못 조정할 것입니다. 또한 정규화된 가중치를 `fit` 함수의 `sample_weight` 매개변수에 전달합니다.

```python
from sklearn.linear_model import ElasticNet

lm = ElasticNet(alpha=0.01, precompute=gram)
lm.fit(X_centered, y, sample_weight=normalized_weights)
```
