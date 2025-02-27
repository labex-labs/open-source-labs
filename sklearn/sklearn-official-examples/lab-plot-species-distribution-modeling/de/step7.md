# AUC berechnen

In diesem Schritt werden wir die Fläche unter der ROC-Kurve (AUC) in Bezug auf Hintergrundpunkte berechnen. Wir werden die Artenverteilung mit den Testdaten und den Hintergrundpunkten vorhersagen und die AUC berechnen.

```python
# Compute AUC with regards to background points
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
print("\n Area under the ROC curve : %f" % roc_auc)
```
