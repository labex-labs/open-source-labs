# Calculer l'affinité de propagation

Nous allons utiliser la classe `AffinityPropagation` du module `sklearn.cluster` pour effectuer un regroupement sur l'ensemble de données. Nous allons définir le paramètre `préférence` sur -50, qui contrôle le nombre de groupes qui seront générés. Une valeur plus faible de `préférence` entraînera la génération de plus de groupes. Nous allons ensuite afficher certaines métriques pour évaluer la qualité du regroupement.

```python
af = AffinityPropagation(preference=-50, random_state=0).fit(X)
cluster_centers_indices = af.cluster_centers_indices_
labels = af.labels_

n_clusters_ = len(cluster_centers_indices)

print("Nombre estimé de groupes : %d" % n_clusters_)
print("Homogénéité : %0.3f" % metrics.homogeneity_score(labels_true, labels))
print("Complétude : %0.3f" % metrics.completeness_score(labels_true, labels))
print("V-mesure : %0.3f" % metrics.v_measure_score(labels_true, labels))
print("Indice de Rand ajusté : %0.3f" % metrics.adjusted_rand_score(labels_true, labels))
print(
    "Information mutuelle ajustée : %0.3f"
    % metrics.adjusted_mutual_info_score(labels_true, labels)
)
print(
    "Coefficient de silhouette : %0.3f"
    % metrics.silhouette_score(X, labels, metric="sqeuclidean")
)
```
