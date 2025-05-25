# 희소 역공분산

희소 역공분산 추정, 또는 공분산 선택은 희소 정밀도 행렬을 추정하는 것을 목표로 합니다. 여기서 공분산 행렬의 역행렬은 부분 상관 행렬을 나타냅니다. `sklearn.covariance` 패키지에는 l1 페널티를 사용하여 희소 역공분산 행렬을 추정하는 `GraphicalLasso` 클래스가 포함되어 있습니다.

```python
from sklearn.covariance import GraphicalLasso

# GraphicalLasso 객체를 생성하고 데이터에 맞춥니다.
graphical_lasso = GraphicalLasso().fit(data)

# 희소 역공분산 행렬을 계산합니다.
sparse_inverse_covariance_matrix = graphical_lasso.precision_
```
