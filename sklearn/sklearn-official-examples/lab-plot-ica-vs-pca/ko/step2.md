# PCA 알고리즘 사용

이 단계에서는 PCA 알고리즘을 사용하여 원시 특징 공간에서 최대 분산을 설명하는 방향에 해당하는 직교 방향을 찾습니다.

```python
pca = PCA()
S_pca_ = pca.fit(X).transform(X)
```
