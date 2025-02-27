# Построение кривых ROC и DET

Мы будем использовать классы `RocCurveDisplay` и `DetCurveDisplay` из scikit - learn для построения кривых ROC и DET соответственно. Функция `RocCurveDisplay.from_estimator` вычисляет кривую ROC и рисует ее на заданной оси. Аналогично, функция `DetCurveDisplay.from_estimator` вычисляет кривую DET и рисует ее на заданной оси. Мы создадим два подграфика, один для кривых ROC и другой для кривых DET, и построим кривые для каждого классификатора.

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
