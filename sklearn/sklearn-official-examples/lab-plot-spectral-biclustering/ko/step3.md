# `SpectralBiclustering` 적용

모델을 적용하고 얻은 클러스터를 실제 클러스터와 비교합니다. 모델을 생성할 때 데이터셋 생성에 사용했던 클러스터 수 (`n_clusters = (4, 3)`) 와 동일한 값을 지정하면 좋은 결과를 얻을 수 있습니다.

```python
from sklearn.cluster import SpectralBiclustering
from sklearn.metrics import consensus_score

model = SpectralBiclustering(n_clusters=n_clusters, method="log", random_state=0)
model.fit(data)

# 두 세트의 바이클러스터 유사성을 계산합니다.
score = consensus_score(
    model.biclusters_, (rows[:, row_idx_shuffled], columns[:, col_idx_shuffled])
)
print(f"consensus score: {score:.1f}")
```
