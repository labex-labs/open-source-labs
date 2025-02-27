# Calcular el AUC

En este paso, calcularemos el área bajo la curva ROC (AUC) en relación con los puntos de fondo. Predeciríamos la distribución de especies utilizando los datos de prueba y los puntos de fondo, y calcularíamos el AUC.

```python
# Calcular el AUC en relación con los puntos de fondo
background_points = np.c_[
    np.random.randint(low=0, high=data.Ny, size=10000),
    np.random.randint(low=0, high=data.Nx, size=10000),
].T

pred_background = Z[background_points[0], background_points[1]]
pred_test = clf.decision_function((BV_bunch.cov_test - mean) / std)
scores = np.r_[pred_test, pred_background]
y = np.r_[np.ones(pred_test.shape), np.zeros(pred_background.shape)]
fpr, tpr, thresholds = metrics.roc_curve(y, scores)
roc_auc = metrics.auc(fpr, tpr)
plt.text(-35, -70, "AUC: %.3f" % roc_auc, ha="right")
print("\n Área bajo la curva ROC : %f" % roc_auc)
```
