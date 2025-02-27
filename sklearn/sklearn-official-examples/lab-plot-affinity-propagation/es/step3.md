# Calcular la Propagación de Afinidad

Utilizaremos la clase `AffinityPropagation` del módulo `sklearn.cluster` para realizar el agrupamiento en el conjunto de datos. Estableceremos el parámetro `preference` en -50, que controla el número de clusters que se generarán. Un valor más bajo de `preference` resultará en la generación de más clusters. Luego, imprimiremos algunas métricas para evaluar la calidad del agrupamiento.

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
