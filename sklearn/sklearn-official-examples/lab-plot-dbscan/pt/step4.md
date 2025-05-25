# Métricas de Avaliação

Podemos usar métricas de avaliação para quantificar a qualidade dos clusters resultantes. Usaremos as métricas de homogeneidade, completude, V-measure, índice Rand ajustado, informação mútua ajustada e coeficiente de silhueta. Acederemos a estas métricas através do módulo `sklearn.metrics`. Se as etiquetas de verdade fundamental não forem conhecidas, a avaliação só pode ser realizada usando os próprios resultados do modelo. Nesse caso, o coeficiente de silhueta é útil.

```python
print(f"Homogeneidade: {metrics.homogeneity_score(labels_true, labels):.3f}")
print(f"Completude: {metrics.completeness_score(labels_true, labels):.3f}")
print(f"V-measure: {metrics.v_measure_score(labels_true, labels):.3f}")
print(f"Índice Rand Ajustado: {metrics.adjusted_rand_score(labels_true, labels):.3f}")
print(f"Informação Mútua Ajustada: {metrics.adjusted_mutual_info_score(labels_true, labels):.3f}")
print(f"Coeficiente de Silhueta: {metrics.silhouette_score(X, labels):.3f}")
```
