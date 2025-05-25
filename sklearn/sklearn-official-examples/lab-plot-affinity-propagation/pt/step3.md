# Calcular Afinidade de Propagação

Usaremos a classe `AffinityPropagation` do módulo `sklearn.cluster` para realizar o agrupamento nos dados. Definiremos o parâmetro `preference` como -50, que controla o número de clusters a serem gerados. Um valor menor de `preference` resultará em mais clusters sendo gerados. Em seguida, imprimiremos algumas métricas para avaliar a qualidade do agrupamento.

```python
af = AffinityPropagation(preference=-50, random_state=0).fit(X)
cluster_centers_indices = af.cluster_centers_indices_
labels = af.labels_

n_clusters_ = len(cluster_centers_indices)

print("Número estimado de clusters: %d" % n_clusters_)
print("Homogeneidade: %0.3f" % metrics.homogeneity_score(labels_true, labels))
print("Completude: %0.3f" % metrics.completeness_score(labels_true, labels))
print("Medida-V: %0.3f" % metrics.v_measure_score(labels_true, labels))
print("Índice Rand Ajustado: %0.3f" % metrics.adjusted_rand_score(labels_true, labels))
print(
    "Informação Mútua Ajustada: %0.3f"
    % metrics.adjusted_mutual_info_score(labels_true, labels)
)
print(
    "Coeficiente de Silhueta: %0.3f"
    % metrics.silhouette_score(X, labels, metric="sqeuclidean")
)
```
