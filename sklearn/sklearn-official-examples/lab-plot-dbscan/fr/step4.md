# Métriques d'évaluation

Nous pouvons utiliser des métriques d'évaluation pour quantifier la qualité des groupes résultants. Nous utiliserons les métriques d'homogénéité, de complétude, de V-mesure, d'indice de Rand ajusté, d'information mutuelle ajustée et de coefficient de silhouette. Nous accéderons à ces métriques à partir du module sklearn.metrics. Si les étiquettes de vérité terrain ne sont pas connues, l'évaluation ne peut être effectuée que à l'aide des résultats du modèle lui-même. Dans ce cas, le coefficient de silhouette est pratique.

```python
print(f"Homogénéité: {metrics.homogeneity_score(labels_true, labels):.3f}")
print(f"Complétude: {metrics.completeness_score(labels_true, labels):.3f}")
print(f"V-mesure: {metrics.v_measure_score(labels_true, labels):.3f}")
print(f"Indice de Rand ajusté: {metrics.adjusted_rand_score(labels_true, labels):.3f}")
print(f"Information mutuelle ajustée: {metrics.adjusted_mutual_info_score(labels_true, labels):.3f}")
print(f"Coefficient de silhouette: {metrics.silhouette_score(X, labels):.3f}")
```
