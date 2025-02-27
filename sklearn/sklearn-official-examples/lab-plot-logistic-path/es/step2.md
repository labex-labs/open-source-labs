# Calcular la trayectoria de regularización

Calcularemos la trayectoria de regularización entrenando modelos de regresión logística penalizados con L1 con diferentes fuerzas de regularización. Usaremos el solucionador liblinear, que puede optimizar eficientemente la pérdida de la regresión logística con una penalización L1. Estableceremos un valor bajo para la tolerancia para asegurarnos de que el modelo haya convergido antes de recopilar los coeficientes. También usaremos warm_start = True, lo que significa que los coeficientes de los modelos se reutilizan para inicializar la siguiente ajuste del modelo para acelerar el cálculo de la trayectoria completa.

```python
import numpy as np
from sklearn import linear_model
from sklearn.svm import l1_min_c

cs = l1_min_c(X, y, loss="log") * np.logspace(0, 10, 16)

clf = linear_model.LogisticRegression(
    penalty="l1",
    solver="liblinear",
    tol=1e-6,
    max_iter=int(1e6),
    warm_start=True,
    intercept_scaling=10000.0,
)
coefs_ = []
for c in cs:
    clf.set_params(C=c)
    clf.fit(X, y)
    coefs_.append(clf.coef_.ravel().copy())

coefs_ = np.array(coefs_)
```
