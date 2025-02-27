# Вычисляем Affinity Propagation

Мы будем использовать класс `AffinityPropagation` из модуля `sklearn.cluster` для кластеризации набора данных. Мы установим параметр `preference` равным -50, который контролирует количество кластеров, которое будет сгенерировано. Более низкое значение `preference` приведет к созданию большего количества кластеров. Затем мы выведем некоторые метрики, чтобы оценить качество кластеризации.

```python
af = AffinityPropagation(preference=-50, random_state=0).fit(X)
cluster_centers_indices = af.cluster_centers_indices_
labels = af.labels_

n_clusters_ = len(cluster_centers_indices)

print("Estimated number of clusters: %d" % n_clusters_)
print("Homogeneity: %0.3f" % metrics.homogeneity_score(labels_true, labels))
print("Completeness: %0.3f" % metrics.completeness_score(labels_true, labels))
print("V-measure: %0.3f" % metrics.v_measure_score(labels_true, labels))
print("Adjusted Rand Index: %0.3f" % metrics.adjusted_rand_score(labels_true, labels))
print(
    "Adjusted Mutual Information: %0.3f"
    % metrics.adjusted_mutual_info_score(labels_true, labels)
)
print(
    "Silhouette Coefficient: %0.3f"
    % metrics.silhouette_score(X, labels, metric="sqeuclidean")
)
```
