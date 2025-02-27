# ROC - und DET - Kurven plotten

Wir werden die Klassen `RocCurveDisplay` und `DetCurveDisplay` von scikit - learn verwenden, um die ROC - und DET - Kurven jeweils zu plotten. Die Funktion `RocCurveDisplay.from_estimator` berechnet die ROC - Kurve und zeigt sie auf der angegebenen Achse an. Ähnlich berechnet die Funktion `DetCurveDisplay.from_estimator` die DET - Kurve und zeigt sie auf der angegebenen Achse an. Wir werden zwei Teilplots erstellen, einen für ROC - Kurven und einen für DET - Kurven, und die Kurven für jeden Klassifizierer plotten.

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
