# Métricas de evaluación

Podemos usar métricas de evaluación para cuantificar la calidad de los clusters resultantes. Usaremos las métricas de homogeneidad, completitud, V-medida, índice de Rand ajustado, información mutua ajustada y coeficiente de silueta. Accederemos a estas métricas desde el módulo sklearn.metrics. Si las etiquetas de verdad básica no son conocidas, la evaluación solo se puede realizar usando los propios resultados del modelo. En ese caso, el coeficiente de silueta resulta útil.

```python
print(f"Homogeneidad: {metrics.homogeneity_score(labels_true, labels):.3f}")
print(f"Completitud: {metrics.completeness_score(labels_true, labels):.3f}")
print(f"V-medida: {metrics.v_measure_score(labels_true, labels):.3f}")
print(f"Índice de Rand Ajustado: {metrics.adjusted_rand_score(labels_true, labels):.3f}")
print(f"Información Mutua Ajustada: {metrics.adjusted_mutual_info_score(labels_true, labels):.3f}")
print(f"Coeficiente de Silueta: {metrics.silhouette_score(X, labels):.3f}")
```
