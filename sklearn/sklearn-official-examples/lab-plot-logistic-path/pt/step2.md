# Calcular o caminho de regularização

Vamos calcular o caminho de regularização treinando modelos de regressão logística penalizados por L1 com diferentes níveis de força de regularização. Usaremos o solucionador liblinear, que pode otimizar eficientemente a perda de Regressão Logística com uma penalidade L1. Definiremos um valor baixo para a tolerância para garantir que o modelo tenha convergido antes de coletar os coeficientes. Também usaremos warm_start=True, o que significa que os coeficientes dos modelos são reutilizados para inicializar o ajuste do próximo modelo, acelerando o cálculo do caminho completo.

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
