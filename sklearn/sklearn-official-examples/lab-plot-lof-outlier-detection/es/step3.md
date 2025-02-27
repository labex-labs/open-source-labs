# Ajustar el modelo para la detección de valores atípicos

Usaremos `LocalOutlierFactor` para ajustar el modelo para la detección de valores atípicos y calcular las etiquetas predichas de las muestras de entrenamiento.

```python
clf = LocalOutlierFactor(n_neighbors=20, contamination=0.1)
y_pred = clf.fit_predict(X)
X_scores = clf.negative_outlier_factor_
```
