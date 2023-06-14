# Plot ROC and DET Curves

We will use scikit-learn's `RocCurveDisplay` and `DetCurveDisplay` classes to plot the ROC and DET curves, respectively. The `RocCurveDisplay.from_estimator` function calculates the ROC curve and plots it on the given axis. Similarly, the `DetCurveDisplay.from_estimator` function calculates the DET curve and plots it on the given axis. We will create two subplots, one for ROC curves and one for DET curves, and plot the curves for each classifier.

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


