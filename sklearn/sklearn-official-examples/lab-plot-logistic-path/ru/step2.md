# Вычисление пути регуляризации

Мы будем вычислять путь регуляризации, обучая модели L1-штрафованной логистической регрессии с разными значениями силы регуляризации. Мы будем использовать решатель liblinear, который может эффективно оптимизировать функцию потерь логистической регрессии с L1-штрафом. Мы установим низкое значение для допустимой погрешности, чтобы убедиться, что модель сойдена, прежде чем собирать коэффициенты. Мы также будем использовать warm_start=True, что означает, что коэффициенты моделей будут переиспользованы для инициализации следующего подбора модели, чтобы ускорить вычисление полного пути.

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
