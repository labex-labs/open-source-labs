# Compute regularization path

We will compute the regularization path by training L1-penalized logistic regression models with different regularization strengths. We will use the liblinear solver, which can efficiently optimize for the Logistic Regression loss with an L1 penalty. We will set a low value for the tolerance to make sure that the model has converged before collecting the coefficients. We will also use warm_start=True, which means that the coefficients of the models are reused to initialize the next model fit to speed-up the computation of the full-path.

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
