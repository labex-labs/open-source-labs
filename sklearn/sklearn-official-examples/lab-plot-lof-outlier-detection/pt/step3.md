# Ajustar o Modelo para Detecção de Outliers

Vamos usar `LocalOutlierFactor` para ajustar o modelo de detecção de outliers e calcular as etiquetas previstas das amostras de treino.

```python
clf = LocalOutlierFactor(n_neighbors=20, contamination=0.1)
y_pred = clf.fit_predict(X)
X_scores = clf.negative_outlier_factor_
```
