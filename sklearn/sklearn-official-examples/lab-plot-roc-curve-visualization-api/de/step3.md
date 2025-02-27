# Einen Random Forest trainieren und die ROC-Kurve zeichnen

In diesem Schritt werden wir einen Random-Forest-Klassifizierer trainieren und seine ROC-Kurve neben der SVC-ROC-Kurve zeichnen. Dazu werden wir ein neues `RandomForestClassifier`-Objekt erstellen, es auf die Trainingsdaten anpassen und dann ein neues `RocCurveDisplay`-Objekt mit diesem Klassifizierer erstellen. Wir werden auch den Parameter `ax` an diese Funktion übergeben, um die Kurven auf der gleichen Achse zu zeichnen. Schließlich werden wir die `plot()`-Methode des `svc_disp`-Objekts aufrufen, um die SVC-ROC-Kurve zu zeichnen.

```python
from sklearn.ensemble import RandomForestClassifier

rfc = RandomForestClassifier(n_estimators=10, random_state=42)
rfc.fit(X_train, y_train)

ax = plt.gca()
rfc_disp = RocCurveDisplay.from_estimator(rfc, X_test, y_test, ax=ax, alpha=0.8)
svc_disp.plot(ax=ax, alpha=0.8)
plt.show()
```
