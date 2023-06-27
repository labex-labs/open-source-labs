# Defining the List of Metrics to Evaluate

We first define a list of metrics to be used to evaluate clustering algorithms. Examples of such metrics are V-measure, Rand index, Adjusted Rand index (ARI), Mutual Information (MI), Normalized Mutual Information (NMI), and Adjusted Mutual Information (AMI).

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
