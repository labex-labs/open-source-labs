# 무작위 SVD 를 사용한 주요 특이 벡터 계산

scikit-learn 에 구현된 `randomized_svd` 메서드를 사용하여 주요 특이 벡터를 계산합니다.

```python
from sklearn.decomposition import randomized_svd

print("무작위 SVD 를 사용하여 주요 특이 벡터를 계산합니다.")
U, s, V = randomized_svd(X, 5, n_iter=3)
```
