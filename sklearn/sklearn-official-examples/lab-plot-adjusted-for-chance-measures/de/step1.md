# Definition der Liste der Metriken zur Bewertung

Wir definieren zunächst eine Liste von Metriken, die zur Bewertung von Clusteralgorithmen verwendet werden sollen. Beispiele solcher Metriken sind V-Measure, Rand-Index, Adjustierter Rand-Index (ARI), gegenseitige Information (MI), normalisierte gegenseitige Information (NMI) und angepasste gegenseitige Information (AMI).

```python
from sklearn import metrics

score_funcs = [
    ("V-Measure", metrics.v_measure_score),
    ("Rand-Index", metrics.rand_score),
    ("ARI", metrics.adjusted_rand_score),
    ("MI", metrics.mutual_info_score),
    ("NMI", metrics.normalized_mutual_info_score),
    ("AMI", metrics.adjusted_mutual_info_score),
]
```
