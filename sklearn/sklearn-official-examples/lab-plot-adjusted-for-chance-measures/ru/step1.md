# Определение списка метрик для оценки

Сначала мы определяем список метрик, которые будут использоваться для оценки алгоритмов кластеризации. Примерами таких метрик являются V-мера, индекс Рэнда, скорректированный индекс Рэнда (ARI), взаимная информация (MI), нормализованная взаимная информация (NMI) и скорректированная взаимная информация (AMI).

```python
from sklearn import metrics

score_funcs = [
    ("V-мера", metrics.v_measure_score),
    ("Индекс Рэнда", metrics.rand_score),
    ("ARI", metrics.adjusted_rand_score),
    ("MI", metrics.mutual_info_score),
    ("NMI", metrics.normalized_mutual_info_score),
    ("AMI", metrics.adjusted_mutual_info_score),
]
```
