# Ajuster le modèle pour la détection d'anomalies

Nous allons utiliser `LocalOutlierFactor` pour ajuster le modèle pour la détection d'anomalies et calculer les étiquettes prédites des échantillons d'entraînement.

```python
clf = LocalOutlierFactor(n_neighbors=20, contamination=0.1)
y_pred = clf.fit_predict(X)
X_scores = clf.negative_outlier_factor_
```
