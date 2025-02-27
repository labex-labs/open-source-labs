# Trazar curvas ROC y DET

Usaremos las clases `RocCurveDisplay` y `DetCurveDisplay` de scikit-learn para trazar las curvas ROC y DET, respectivamente. La función `RocCurveDisplay.from_estimator` calcula la curva ROC y la traza en el eje dado. Del mismo modo, la función `DetCurveDisplay.from_estimator` calcula la curva DET y la traza en el eje dado. Crearemos dos subgráficos, uno para las curvas ROC y otro para las curvas DET, y trazaremos las curvas para cada clasificador.

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
