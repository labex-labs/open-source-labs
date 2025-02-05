# Evaluation Metrics

We can use evaluation metrics to quantify the quality of the resulting clusters. We will use the homogeneity, completeness, V-measure, adjusted Rand index, adjusted mutual information, and silhouette coefficient metrics. We will access these metrics from the sklearn.metrics module. If the ground truth labels are not known, evaluation can only be performed using the model results itself. In that case, the silhouette coefficient comes in handy.

```python
print(f"Homogeneity: {metrics.homogeneity_score(labels_true, labels):.3f}")
print(f"Completeness: {metrics.completeness_score(labels_true, labels):.3f}")
print(f"V-measure: {metrics.v_measure_score(labels_true, labels):.3f}")
print(f"Adjusted Rand Index: {metrics.adjusted_rand_score(labels_true, labels):.3f}")
print(f"Adjusted Mutual Information: {metrics.adjusted_mutual_info_score(labels_true, labels):.3f}")
print(f"Silhouette Coefficient: {metrics.silhouette_score(X, labels):.3f}")
```
