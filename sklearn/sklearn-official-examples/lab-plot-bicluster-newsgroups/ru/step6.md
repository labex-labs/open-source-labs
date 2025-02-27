# Бикластеризация с использованием алгоритма спектральной кокластеризации

Мы выполним бикластеризацию с использованием алгоритма спектральной кокластеризации, определив кокластер и подгоняя его под данные.

```python
cocluster = SpectralCoclustering(
    n_clusters=len(categories), svd_method="arpack", random_state=0
)
cocluster.fit(X)
y_cocluster = cocluster.row_labels_
```
