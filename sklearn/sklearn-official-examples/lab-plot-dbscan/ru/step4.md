# Метрики оценки

Мы можем использовать метрики оценки, чтобы количественно оценить качество полученных кластеров. Мы будем использовать метрики однородности, полноты, V-мера, скорректированный индекс Рэнда, скорректированную взаимную информацию и коэффициент силуэта. Мы будем получать эти метрики из модуля sklearn.metrics. Если истинные метки неизвестны, оценку можно проводить только на основе результатов модели. В этом случае коэффициент силуэта оказывается полезным.

```python
print(f"Homogeneity: {metrics.homogeneity_score(labels_true, labels):.3f}")
print(f"Completeness: {metrics.completeness_score(labels_true, labels):.3f}")
print(f"V-measure: {metrics.v_measure_score(labels_true, labels):.3f}")
print(f"Adjusted Rand Index: {metrics.adjusted_rand_score(labels_true, labels):.3f}")
print(f"Adjusted Mutual Information: {metrics.adjusted_mutual_info_score(labels_true, labels):.3f}")
print(f"Silhouette Coefficient: {metrics.silhouette_score(X, labels):.3f}")
```
