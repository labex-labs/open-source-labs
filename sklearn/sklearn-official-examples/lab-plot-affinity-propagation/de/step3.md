# Berechnung der Affinitätsfortpflanzung

Wir werden die Klasse `AffinityPropagation` aus dem Modul `sklearn.cluster` verwenden, um die Clusteranalyse auf dem Datensatz durchzuführen. Wir werden den Parameter `preference` auf -50 setzen, der die Anzahl der zu erzeugenden Cluster steuert. Ein niedrigerer Wert von `preference` führt zu mehr erzeugten Clustern. Anschließend werden wir einige Metriken ausgeben, um die Qualität der Clusterbildung zu bewerten.

```python
af = AffinityPropagation(preference=-50, random_state=0).fit(X)
cluster_centers_indices = af.cluster_centers_indices_
labels = af.labels_

n_clusters_ = len(cluster_centers_indices)

print("Geschätzte Anzahl der Cluster: %d" % n_clusters_)
print("Homogenität: %0.3f" % metrics.homogeneity_score(labels_true, labels))
print("Vollständigkeit: %0.3f" % metrics.completeness_score(labels_true, labels))
print("V-Maß: %0.3f" % metrics.v_measure_score(labels_true, labels))
print("Angepasster Rand-Index: %0.3f" % metrics.adjusted_rand_score(labels_true, labels))
print(
    "Angepasste gegenseitige Information: %0.3f"
    % metrics.adjusted_mutual_info_score(labels_true, labels)
)
print(
    "Silhouettenkoeffizient: %0.3f"
    % metrics.silhouette_score(X, labels, metric="sqeuclidean")
)
```
