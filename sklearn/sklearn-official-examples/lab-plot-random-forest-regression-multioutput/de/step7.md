# Ergebnisse grafisch darstellen

Wir werden die Ergebnisse grafisch darstellen, um die Leistung der beiden Regressoren zu vergleichen. Wir werden `matplotlib` verwenden, um einen Streudiagramm der tatsächlichen Testdaten, der Vorhersagen des Random Forest Regressors und der Vorhersagen des Multi-Output Regressors zu erstellen.

```python
plt.figure()
s = 50
a = 0.4
plt.scatter(y_test[:, 0], y_test[:, 1], edgecolor="k", c="navy", s=s, marker="s", alpha=a, label="Data")
plt.scatter(y_rf[:, 0], y_rf[:, 1], edgecolor="k", c="c", s=s, marker="^", alpha=a, label="RF score=%.2f" % regr_rf.score(X_test, y_test))
plt.scatter(y_multirf[:, 0], y_multirf[:, 1], edgecolor="k", c="cornflowerblue", s=s, alpha=a, label="Multi RF score=%.2f" % regr_multirf.score(X_test, y_test))
plt.xlim([-6, 6])
plt.ylim([-6, 6])
plt.xlabel("target 1")
plt.ylabel("target 2")
plt.title("Comparing Random Forests and the Multi-Output Meta Estimator")
plt.legend()
plt.show()
```
