# 특징 응집 수행

이 단계에서는 scikit-learn 의 `FeatureAgglomeration` 클래스를 사용하여 특징 응집을 수행합니다. 클러스터 수는 32 개로 설정합니다.

```python
agglo = cluster.FeatureAgglomeration(connectivity=connectivity, n_clusters=32)
agglo.fit(X)
X_reduced = agglo.transform(X)
```
