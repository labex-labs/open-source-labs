# 스펙트럴 공동 클러스터링 알고리즘 적용

5 개의 클러스터를 사용하여 섞인 데이터셋에 스펙트럴 공동 클러스터링 (Spectral Co-Clustering) 알고리즘을 적용합니다.

```python
model = SpectralCoclustering(n_clusters=5, random_state=0)
model.fit(data)
```
