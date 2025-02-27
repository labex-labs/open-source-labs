# Evaluationsmetriken

Wir können Evaluationsmetriken verwenden, um die Qualität der resultierenden Cluster zu quantifizieren. Wir werden die Homogenität, Vollständigkeit, V-Maß, angepassten Randindex, angepasste gegenseitige Information und Silhouettenkoeffizient-Metriken verwenden. Wir werden diese Metriken aus dem sklearn.metrics-Modul zugreifen. Wenn die wahren Labels unbekannt sind, kann die Evaluation nur mithilfe der Modellresultate selbst durchgeführt werden. In diesem Fall kommt der Silhouettenkoeffizient sehr praktisch.

```python
print(f"Homogenität: {metrics.homogeneity_score(labels_true, labels):.3f}")
print(f"Vollständigkeit: {metrics.completeness_score(labels_true, labels):.3f}")
print(f"V-Maß: {metrics.v_measure_score(labels_true, labels):.3f}")
print(f"Angepasster Randindex: {metrics.adjusted_rand_score(labels_true, labels):.3f}")
print(f"Angepasste gegenseitige Information: {metrics.adjusted_mutual_info_score(labels_true, labels):.3f}")
print(f"Silhouettenkoeffizient: {metrics.silhouette_score(X, labels):.3f}")
```
