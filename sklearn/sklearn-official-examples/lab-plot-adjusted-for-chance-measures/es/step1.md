# Definiendo la lista de métricas para evaluar

Primero definimos una lista de métricas que se utilizarán para evaluar los algoritmos de clustering. Ejemplos de tales métricas son la V-medida, el índice Rand, el índice Rand ajustado (ARI), la información mutua (MI), la información mutua normalizada (NMI) y la información mutua ajustada (AMI).

```python
from sklearn import metrics

score_funcs = [
    ("V-medida", metrics.v_measure_score),
    ("Índice Rand", metrics.rand_score),
    ("ARI", metrics.adjusted_rand_score),
    ("MI", metrics.mutual_info_score),
    ("NMI", metrics.normalized_mutual_info_score),
    ("AMI", metrics.adjusted_mutual_info_score),
]
```
