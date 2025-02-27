# Modell für die Ausreißerdetektion anpassen

Wir werden `LocalOutlierFactor` verwenden, um das Modell für die Ausreißerdetektion anzupassen und die vorhergesagten labels der trainsierungsstichproben zu berechnen.

```python
clf = LocalOutlierFactor(n_neighbors=20, contamination=0.1)
y_pred = clf.fit_predict(X)
X_scores = clf.negative_outlier_factor_
```
