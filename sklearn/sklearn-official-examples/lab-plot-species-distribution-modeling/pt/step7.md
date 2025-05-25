# Calcular AUC

Neste passo, calcularemos a área sob a curva ROC (AUC) em relação aos pontos de fundo. Predizeremos a distribuição da espécie usando os dados de teste e os pontos de fundo, e calcularemos a AUC.

```python
# Calcular AUC em relação aos pontos de fundo
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
print("\n Área sob a curva ROC : %f" % roc_auc)
```
