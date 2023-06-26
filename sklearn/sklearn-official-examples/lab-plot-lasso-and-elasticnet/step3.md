# Automatic Relevance Determination (ARD)

An ARD regression is the Bayesian version of the Lasso. It can produce interval estimates for all of the parameters, including the error variance, if required. It is a suitable option when the signals have Gaussian noise.

```python
from sklearn.linear_model import ARDRegression

t0 = time()
ard = ARDRegression().fit(X_train, y_train)
print(f"ARD fit done in {(time() - t0):.3f}s")

y_pred_ard = ard.predict(X_test)
r2_score_ard = r2_score(y_test, y_pred_ard)
print(f"ARD r^2 on test data : {r2_score_ard:.3f}")
```
