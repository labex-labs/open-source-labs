# Plotar Curvas ROC e DET

Usaremos as classes `RocCurveDisplay` e `DetCurveDisplay` do scikit-learn para plotar as curvas ROC e DET, respectivamente. A função `RocCurveDisplay.from_estimator` calcula a curva ROC e a plota no eixo fornecido. Similarmente, a função `DetCurveDisplay.from_estimator` calcula a curva DET e a plota no eixo fornecido. Criaremos dois subplots, um para as curvas ROC e outro para as curvas DET, e plotaremos as curvas para cada classificador.

```python
import matplotlib.pyplot as plt
from sklearn.metrics import DetCurveDisplay, RocCurveDisplay

fig, [ax_roc, ax_det] = plt.subplots(1, 2, figsize=(11, 5))

for name, clf in classifiers.items():
    clf.fit(X_train, y_train)

    RocCurveDisplay.from_estimator(clf, X_test, y_test, ax=ax_roc, name=name)
    DetCurveDisplay.from_estimator(clf, X_test, y_test, ax=ax_det, name=name)

ax_roc.set_title("Curvas Característica Operacional do Receptor (ROC)")
ax_det.set_title("Curvas de Comércio de Erros de Detecção (DET)")

ax_roc.grid(linestyle="--")
ax_det.grid(linestyle="--")

plt.legend()
plt.show()
```
