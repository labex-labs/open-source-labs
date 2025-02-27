# Вычисление кластеризации

После определения данных и матрицы связности мы можем теперь выполнить иерархическую кластеризацию. Мы будем использовать класс `AgglomerativeClustering` из scikit-learn для выполнения кластеризации. Мы установим количество кластеров в 27, что соответствует количеству монет на изображении. Мы будем использовать метод связи "ward", который минимизирует дисперсию расстояний между объединяемыми кластерами. Мы также передадим матрицу связности, которую создали на шаге 2.

```python
from sklearn.cluster import AgglomerativeClustering
import time as time

print("Compute structured hierarchical clustering...")
st = time.time()
n_clusters = 27  # number of regions
ward = AgglomerativeClustering(
    n_clusters=n_clusters, linkage="ward", connectivity=connectivity
)
ward.fit(X)
label = np.reshape(ward.labels_, rescaled_coins.shape)
print(f"Elapsed time: {time.time() - st:.3f}s")
print(f"Number of pixels: {label.size}")
print(f"Number of clusters: {np.unique(label).size}")
```
