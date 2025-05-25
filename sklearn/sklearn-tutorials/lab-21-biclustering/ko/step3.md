# 스펙트럼 양분할 군집화 수행

다음으로, 스펙트럼 양분할 군집화 (Spectral Biclustering) 알고리즘을 사용하여 양분할 군집화를 수행합니다. 이 알고리즘은 데이터 행렬에 숨겨진 체커보드 구조가 있다고 가정합니다.

```python
# 스펙트럼 양분할 군집화 모델 초기화 및 적합
model_bi = SpectralBiclustering(n_clusters=(2, 3), random_state=0)
model_bi.fit(data)

# 행 및 열 군집 멤버십 가져오기
row_clusters_bi = model_bi.row_labels_
column_clusters_bi = model_bi.column_labels_
```
