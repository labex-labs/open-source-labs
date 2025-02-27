# Tracer les courbes ROC et DET

Nous utiliserons les classes `RocCurveDisplay` et `DetCurveDisplay` de scikit-learn pour tracer respectivement les courbes ROC et DET. La fonction `RocCurveDisplay.from_estimator` calcule la courbe ROC et la trace sur l'axe donné. De manière similaire, la fonction `DetCurveDisplay.from_estimator` calcule la courbe DET et la trace sur l'axe donné. Nous allons créer deux sous-graphiques, l'un pour les courbes ROC et l'autre pour les courbes DET, et tracer les courbes pour chaque classifieur.

```python
import matplotlib.pyplot as plt
from sklearn.metrics import DetCurveDisplay, RocCurveDisplay

fig, [ax_roc, ax_det] = plt.subplots(1, 2, figsize=(11, 5))

for name, clf in classifiers.items():
    clf.fit(X_train, y_train)

    RocCurveDisplay.from_estimator(clf, X_test, y_test, ax=ax_roc, name=name)
    DetCurveDisplay.from_estimator(clf, X_test, y_test, ax=ax_det, name=name)

ax_roc.set_title("Receiver Operating Characteristic (ROC) curves")
ax_det.set_title("Detection Error Tradeoff (DET) curves")

ax_roc.grid(linestyle="--")
ax_det.grid(linestyle="--")

plt.legend()
plt.show()
```
