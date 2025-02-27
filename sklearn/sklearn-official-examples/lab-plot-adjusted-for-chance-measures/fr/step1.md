# Définition de la liste de métriques à évaluer

Nous définissons tout d'abord une liste de métriques à utiliser pour évaluer les algorithmes de regroupement. Parmi les exemples de telles métriques, on trouve la mesure V, l'indice de Rand, l'indice de Rand ajusté (ARI), l'information mutuelle (MI), l'information mutuelle normalisée (NMI) et l'information mutuelle ajustée (AMI).

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
