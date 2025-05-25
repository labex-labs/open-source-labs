# 스펙트럼 공동 군집화 수행

이제 스펙트럼 공동 군집화 (Spectral Co-Clustering) 알고리즘을 사용하여 양분할 군집화를 수행합니다. 이 알고리즘은 다른 행과 열에 비해 값이 높은 양분할 군집을 찾습니다.

```python
# 스펙트럼 공동 군집화 모델 초기화 및 적합
model_co = SpectralCoclustering(n_clusters=3, random_state=0)
model_co.fit(data)

# 행 및 열 군집 멤버십 가져오기
row_clusters_co = model_co.row_labels_
column_clusters_co = model_co.column_labels_
```
