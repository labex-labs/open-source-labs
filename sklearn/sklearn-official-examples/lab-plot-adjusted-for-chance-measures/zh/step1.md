# 定义用于评估的指标列表

我们首先定义一个用于评估聚类算法的指标列表。这类指标的示例包括 V 度量、兰德指数、调整兰德指数（ARI）、互信息（MI）、归一化互信息（NMI）和调整互信息（AMI）。

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
