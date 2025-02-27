# Berechne den Regularisierungspfad

Wir werden den Regularisierungspfad berechnen, indem wir L1-penalisierte logistische Regressionsmodelle mit unterschiedlichen Regularisierungsstärken trainieren. Wir werden den liblinear-Löser verwenden, der effizient für die Logistische-Regressionsverlustfunktion mit einer L1-Strafe optimiert werden kann. Wir werden einen niedrigen Wert für die Toleranz setzen, um sicherzustellen, dass das Modell konvergiert ist, bevor die Koeffizienten gesammelt werden. Wir werden auch warm_start=True verwenden, was bedeutet, dass die Koeffizienten der Modelle wiederverwendet werden, um die Initialisierung des nächsten Modellfits zu beschleunigen und die Berechnung des vollen Pfads zu beschleunigen.

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
