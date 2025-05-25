# Definindo a Lista de Métricas para Avaliação

Primeiro, definimos uma lista de métricas a serem usadas para avaliar algoritmos de agrupamento. Exemplos de tais métricas são a medida V, o índice Rand, o índice Rand Ajustado (ARI), a Informação Mútua (MI), a Informação Mútua Normalizada (NMI) e a Informação Mútua Ajustada (AMI).

```python
from sklearn import metrics

score_funcs = [
    ("Medida V", metrics.v_measure_score),
    ("Índice Rand", metrics.rand_score),
    ("ARI", metrics.adjusted_rand_score),
    ("MI", metrics.mutual_info_score),
    ("NMI", metrics.normalized_mutual_info_score),
    ("AMI", metrics.adjusted_mutual_info_score),
]
```
