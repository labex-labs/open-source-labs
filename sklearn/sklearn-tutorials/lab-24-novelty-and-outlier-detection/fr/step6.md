# Accéder aux scores d'anomalie

En plus de prédire les anomalies, nous pouvons également accéder aux scores d'anomalie pour chaque observation en utilisant l'attribut `negative_outlier_factor_`. Des scores d'anomalie plus bas indiquent une plus grande anomalie.

```python
outlier_scores = estimator.negative_outlier_factor_
print(outlier_scores)
```
