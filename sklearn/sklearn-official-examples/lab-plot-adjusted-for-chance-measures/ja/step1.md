# 評価するメトリックのリストを定義する

まず、クラスタリングアルゴリズムを評価するために使用するメトリックのリストを定義します。このようなメトリックの例としては、V-measure、Rand index、調整済み Rand index (ARI)、相互情報 (MI)、正規化相互情報 (NMI)、および調整済み相互情報 (AMI) が挙げられます。

```python
from sklearn import metrics

score_funcs = [
    ("V-measure", metrics.v_measure_score),
    ("Rand index", metrics.rand_score),
    ("ARI", metrics.adjusted_rand_score),
    ("MI", metrics.mutual_info_score),
    ("NMI", metrics.normalized_mutual_info_score),
    ("AMI", metrics.adjusted_mutual_info_score),
]
```
