# Lasso

In this step, we will demonstrate how to use Lasso regression model to estimate the sparse coefficients of the dataset. We will use a fixed value of the regularization parameter `alpha`. In practice, the optimal parameter `alpha` should be selected by passing a `TimeSeriesSplit` cross-validation strategy to a `LassoCV`. To keep the example simple and fast to execute, we directly set the optimal value for alpha here.

```python
from sklearn.linear_model import Lasso
from sklearn.metrics import r2_score
from time import time

t0 = time()
lasso = Lasso(alpha=0.14).fit(X_train, y_train)
print(f"Lasso fit done in {(time() - t0):.3f}s")

y_pred_lasso = lasso.predict(X_test)
r2_score_lasso = r2_score(y_test, y_pred_lasso)
print(f"Lasso r^2 on test data : {r2_score_lasso:.3f}")
```
