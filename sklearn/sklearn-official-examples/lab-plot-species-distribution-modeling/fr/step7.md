# Calculer l'AUC

Dans cette étape, nous allons calculer l'aire sous la courbe ROC (AUC) par rapport aux points d'arrière-plan. Nous allons prédire la distribution d'espèces en utilisant les données de test et les points d'arrière-plan, puis calculer l'AUC.

```python
# Calculer l'AUC par rapport aux points d'arrière-plan
background_points = np.c_[
    np.random.randint(low=0, high=data.Ny, size=10000),
    np.random.randint(low=0, high=data.Nx, size=10000),
].T

pred_background = Z[background_points[0], background_points[1]]
pred_test = clf.decision_function((BV_bunch.cov_test - mean) / std)
scores = np.r_[pred_test, pred_background]
y = np.r_[np.ones(pred_test.shape), np.zeros(pred_background.shape)]
fpr, tpr, seuils = metrics.roc_curve(y, scores)
roc_auc = metrics.auc(fpr, tpr)
plt.text(-35, -70, "AUC: %.3f" % roc_auc, ha="right")
print("\n Aire sous la courbe ROC : %f" % roc_auc)
```
