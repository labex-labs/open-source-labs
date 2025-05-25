# RandomTreesEmbedding 을 이용한 데이터 변환

이 단계에서는 `RandomTreesEmbedding`을 사용하여 데이터를 변환합니다.

```python
hasher = RandomTreesEmbedding(n_estimators=10, random_state=0, max_depth=3)
X_transformed = hasher.fit_transform(X)
```
