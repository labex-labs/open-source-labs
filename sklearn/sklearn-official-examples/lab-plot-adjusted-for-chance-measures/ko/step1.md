# 평가할 지표 목록 정의

먼저 클러스터링 알고리즘을 평가하는 데 사용할 지표 목록을 정의합니다. 이러한 지표의 예로는 V-측도, 랜드 지수, 조정된 랜드 지수 (ARI), 상호 정보 (MI), 정규화된 상호 정보 (NMI), 조정된 상호 정보 (AMI) 가 있습니다.

```python
from sklearn import metrics

score_funcs = [
    ("V-측도", metrics.v_measure_score),
    ("랜드 지수", metrics.rand_score),
    ("ARI", metrics.adjusted_rand_score),
    ("MI", metrics.mutual_info_score),
    ("NMI", metrics.normalized_mutual_info_score),
    ("AMI", metrics.adjusted_mutual_info_score),
]
```
